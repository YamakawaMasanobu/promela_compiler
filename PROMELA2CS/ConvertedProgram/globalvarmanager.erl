% -module(globalvarmanager).
% -export([loop/0]).

% loop() ->
%     receive
%         {From, fin} ->
%             From ! {self(), get()};
%         {From, {reg, Varname, Value}} ->
%             put(Varname, Value),
%             From ! {self(), fin},
%             loop();
%         {From, {get, Varname}} ->
%             Return = get(Varname),
%             % io:format("Varname:~pReturn:~pn", [Varname, Return]),
%             From ! {self(), Return},
%             loop()
%     end.

-module(globalvarmanager).
-export([loop/1]).

loop(WaitPidQueue) ->
    Result = dequeue(WaitPidQueue),
    case Result of
        empty ->
            receive
                {From, fin} ->
                    From ! {self(), get()};
                {From, {reg, Varname, Value}} ->
                    put(Varname, Value),
                    From ! {self(), fin},
                    loop(WaitPidQueue);
                {From, {get, Varname}} ->
                    Return = get(Varname),
                    From ! {self(), Return},
                    loop(WaitPidQueue);
                {From, {selfassign, Varname}} ->
                    Return = get(Varname),
                    From ! {self(), Return},
                    selfassign(From, WaitPidQueue)
            end;
        {Msg, NewWaitPidQueue} ->
            case Msg of
                {From, fin} ->
                    From ! {self(), get()};
                {From, {reg, Varname, Value}} ->
                    put(Varname, Value),
                    From ! {self(), fin},
                    loop(NewWaitPidQueue);
                {From, {get, Varname}} ->
                    Return = get(Varname),
                    From ! {self(), Return},
                    loop(NewWaitPidQueue);
                {From, {selfassign, Varname}} ->
                    Return = get(Varname),
                    From ! {self(), Return},
                    selfassign(From, NewWaitPidQueue)
            end
    end.

selfassign(From, WaitPidQueue) ->
    receive
        {From, {reg, Varname, Value}} ->
            put(Varname, Value),
            From ! {self(), fin},
            loop(WaitPidQueue);
        {OtherPid, Msg} ->
            NewWaitPidQueue = enqueue(WaitPidQueue, {OtherPid, Msg}),
            selfassign(From, NewWaitPidQueue)
    end.



%Queueのためのユーティリティー関数
enqueue(Queue, Value) ->
    Queue ++ [Value].

dequeue(Queue) ->
    case Queue of
        [] ->
            empty;
        [H|T] ->
            {H, T}
    end.
