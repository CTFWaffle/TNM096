%====================================================================
% Logistic PROBLEM

% ACTIONS:    action(Name,Prec,Del,Add)
% Action order: linear

% To run this example:
% 1. consult pop.pl
% 2. consult logistic.pl
% 3. run the query:  ?- plan.


% Defines the type of order; ordering(linear) or ordering(partial)
ordering(linear).

% If the order is partial, you need to define the actions executable in parallel
% most general form:
% Any different actions X and Y are executable in parallel
%     parallel(X,Y) :- X\=Y.

% Strict form of parallelism:
parallel(X,Y) :- X =.. [F|_], Y =.. [F|_], F=load,!.
parallel(X,Y) :- X =.. [F|_], Y =.. [F|_], F=unload,!.

% parallel(X,Y) :- X =.. [P|_], Y =.. [Q|_], P\=Q.


% Load item O into P at Location
action(load(O,P,Loc),
        [item_at(O,Loc),at(P,Loc)],
        [item_at(O,Loc)],
        [inside(O,P)]).

% Unload item O into P at Location
action(unload(O,P,Loc),
        [inside(O,P),at(P,Loc)],
        [inside(O,P)],
        [item_at(O,Loc)]).

% Fly the aircraft to another location if there is fuel
action(fly(P , From,To),
        [at(P,From),has_fuel(P),flight(From,To)],
        [at(P,From),has_fuel(P)],
        [at(P,To),no_fuel(P)]).

% Re-fuel aircraft
action(refuel(P),
        [no_fuel(P),at(P,Loc)],
        [no_fuel(P)],
        [has_fuel(P)]).


% FLUENT
% are properties that can change through execution of action
fluent(at(_,_)).
fluent(item_at(_,_)).
fluent(has_fuel(_)).
fluent(no_fuel(_)).
fluent(inside(_,_)).


% DOMAIN KNOWLEDGE
% static knowledge in rule format: head <- [atom1,atom2,...].

flight(napoli,paris) <- [].
flight(paris,napoli) <- [].

flight(napoli,kopenhagen) <- [].
flight(kopenhagen,napoli) <- [].

flight(norrkoping,kopenhagen) <- [].
flight(kopenhagen,norrkoping) <- [].

flight(berlin,kopenhagen) <- [].
flight(kopenhagen,berlin) <- [].


% INITIAL SITUATION
holds(item_at(pizza,napoli),init).
holds(item_at(ice_cream,kopenhagen),init).
holds(at(pierForceTwo747,napoli),init).
holds(has_fuel(pierForceTwo747),init).

goal([item_at(pizza,norrkoping),item_at(ice_cream,norrkoping)]).

plan :- goal(G), solve(G,9).
