%====================================================================
% SHOPPING PROBLEM

% CONTROL PARAMETERS
ordering(linear).
derivedPlans(one).

% ACTIONS:    action(Name,Prec,Del,Add)

% Agent A buys item X at the Store
action(buy(A,W,Store),
	[store(Store),at(A,Store),sells(Store,W)],
	[],
	[has(A,W)]).

% Agent A goes from location X to location Y
action(go(A,X,Y),
	[location(X),location(Y),X\=Y,at(A,X)],
	[at(A,X)],
	[at(A,Y)]).

% FLUENT
fluent(at(_,_)).
fluent(has(_,_)).

% DOMAIN KNOWLEDGE
store(ica) <- [].
store(clasohlson) <- [].
sells(ica,banana) <- [].
sells(ica,bread) <- [].
sells(ica,cheese) <- [].
sells(clasohlson,drill) <- [].
location(home) <- [].
location(office) <- [].
location(X) <- [store(X)].

% INITIAL SITUATION
holds(at(chris,home),init).
