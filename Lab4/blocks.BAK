
%   Blocks World

%  To run this example, first consult the planner you want to use
%  (strips.pl, idstrips.pl or exstrips.pl) and then consult the blocks.pl example
%  In the query window, run the goal:
%  ?- plan.


:-use_module(library(clpfd)).
:-style_check(-singleton).

% Constraints
table(0). % Table has to be a number due to library
block(X) :- X in 2 .. 4 \/ 6.
pyramid(X) :- X in 1 \/ 5.
orange(X) :-X in 1 \/ 4.
green(X) :- X in 2 \/ 5.
blue(X) :- X in 3 \/ 6.


% Actions
act( moveObject(X, A, B),                             % action name
     [available(X), available(B)],  % preconditions
     [on(X, A), available(B)],                      % delete
     [on(X,B), available(A)]                                    % add
     ):-
     block(B),  % B is a Block
     A #\=B.  % A and B are not the same spot

act(  placeObject(X,From),
     [available(X), on(X,From)],
     [on(X,From)],
     [on(X,0), available(From)]
     ):-
     From #\= 0.


goal_state([on(X,Y),on(Y,Z)]):-
green(Y),
blue(Z).



initial_state([on(1,0),on(2,0),on(3,4),on(4,0),on(5,6),on(6,0), available(1),available(2),available(3),available(5)]).

no_forbidden_states.
