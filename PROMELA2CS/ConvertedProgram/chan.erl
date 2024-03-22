-module(chan).
-export([loop/3]).

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

%チャネルを再現する関数
loop(Queue, WaitPidQueue, SendPidQueue) ->
    io:format("Queue: ~p ~p ~p ~p ~n", [Queue, WaitPidQueue, SendPidQueue, self()]),
    timer:sleep(1000),
    receive
        %finが送られてきた場合は終了する
        {From, fin} ->
            From ! {self(), ok};
        %{send, 値}のタプルが送られてきた場合
        {From, {send, Value}} ->
            % io:format("send: ~p ~p~n", [Value, self()]),
            case Queue of
                [] ->
                    % TmpQueue = enqueue(Queue, Value),
                    % io:format("enqueue ~p ~p~n", [TmpQueue, self()]),
                    % From ! {self(), ok},
                    case WaitPidQueue of
                        [] ->
                            TmpSendPidQueue = enqueue(SendPidQueue, {From,Value}),
                            loop(Queue, WaitPidQueue, TmpSendPidQueue);
                        _ ->
                            % TmpQueue = enqueue(Queue, Value),
                            % {Pidtuple, NewWaitPidQueue} = dequeue(WaitPidQueue),
                            % {Value, NewQueue} = dequeue(TmpQueue),
                            Judge = lists:filter(fun(X) -> {_, const, TmpValue} = X, TmpValue == Value end, WaitPidQueue),
                            case Judge of
                                [] ->
                                    TmpSendPidQueue = enqueue(SendPidQueue, {From,Value}),
                                    loop(Queue, WaitPidQueue, TmpSendPidQueue);
                                [{Pid, const, _}|_] ->
                                    From ! {self(), ok},
                                    Pid ! {self(), {true, Value}},
                                    NewWaitPidQueue = lists:delete({Pid, const, Value}, WaitPidQueue),
                                    loop(Queue, NewWaitPidQueue, SendPidQueue)
                            end
                            % case Pidtuple of
                            %     {Pid, var, Var} ->
                            %         Pid ! {self(), {true, {Var, Value}}},
                            %         loop(NewQueue, NewWaitPidQueue, SendPidQueue);
                            %     {Pid, const, Value} ->
                            %         Pid ! {self(), {true, Value}},
                            %         loop(NewQueue, NewWaitPidQueue, SendPidQueue)
                            %     % {Pid, const, _} ->
                            %     %     loop(TmpQueue, WaitPidQueue, SendPidQueue)
                            % end
                    end;
                [_|_] -> 
                    TmpSendPidQueue = enqueue(SendPidQueue, {From,Value}),
                    loop(Queue, WaitPidQueue, TmpSendPidQueue)
                end;
        {From, {rcv, {const, Const}}} ->
            % io:format("receive: ~p ~p~n", [Const, self()]),
            Result = dequeue(Queue),
            case Result of
                empty ->
                    Judge = lists:filter(fun(X) -> {_, TmpValue} = X, TmpValue == Const end, SendPidQueue),
                    case Judge of
                        [] ->
                            NewWaitPidQueue = enqueue(WaitPidQueue, {From, const, Const}),
                            loop(Queue, NewWaitPidQueue, SendPidQueue);
                        [{SendFrom,SendValue}|_] ->
                            case Const == SendValue of
                                true ->
                                    SendFrom ! {self(), ok},
                                    From ! {self(), {true, SendValue}},
                                    NewSendPidQueue = lists:delete({SendFrom,SendValue}, SendPidQueue),
                                    loop(Queue, WaitPidQueue, NewSendPidQueue);
                                false ->
                                    NewWaitPidQueue = enqueue(WaitPidQueue, {From, const, Const}),
                                    loop(Queue, NewWaitPidQueue, SendPidQueue)
                            end
                        end;
                {Const, NewQueue} ->
                    From ! {self(), {true, Const}},
                    case SendPidQueue of 
                        [] -> 
                            loop(NewQueue, WaitPidQueue, SendPidQueue);
                        [{SendFrom,SendValue}|Tail] ->
                            SendFrom ! {self(), ok},
                            TmpQueue = enqueue(Queue, SendValue),
                            loop(TmpQueue, WaitPidQueue, Tail)
                        end
                % _ ->
                %     NewWaitPidQueue = enqueue(WaitPidQueue, {From, const, Const}),
                %     loop(Queue, NewWaitPidQueue, SendPidQueue)
            end;
        {From, {rcv, {var, Var}}} ->
            Result = dequeue(Queue),
            case Result of
                empty ->
                    NewWaitPidQueue = enqueue(WaitPidQueue, {From, var, Var}),
                    loop(Queue, NewWaitPidQueue, SendPidQueue);
                {Value, NewQueue} ->
                    From ! {self(), {true, {Var, Value}}},
                    loop(NewQueue, WaitPidQueue, SendPidQueue)
            end
    end.