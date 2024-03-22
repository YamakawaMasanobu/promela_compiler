-module(erlutility).
-export([sender/2, receiver/2, guardreceiver/2]).

sender(Value, Pid) ->
    Pid ! {self(), {send, Value}},
    receive
        {Pid, ok} ->
            ok
    end.

receiver(Msg, Pid) ->
    Pid ! {self(), {rcv, Msg}},
    receive
        {Pid, {true, Result}} ->
            {true, Result}
        % {Pid, {false, _}} ->
        %     false
    end.

guardreceiver(Msg, Pid) ->
    Pid ! {self(), {rcv, Msg}},
    receive
        {Pid, {true, Result}} ->
            {true, Result};
        {Pid, {false, _}} ->
            false
    after 5000 ->
        false
    end.