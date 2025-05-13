% Actions

%  Action: Go
act(go(From, To),
[shakey(S), at(S, From), on(S,floor),binding(From, To)], % Is shakey at_ & on_ with loc connected
[at(S, From)], % Remove shakey(S) from "from-location"
[at(S, To)] % Place shakey(S) in to
).

%  Action: Push Box
act( pushBox(B, From, To), % Box B, From location, To location
[shakey(S), box(B),at(S, From), at(B, From), on(S, floor), binding(From, To)], % We have a Shakey & a Box, both at From, shakey is on the floor, rooms are connected.
[at(S, From), at(B,From)], % Remove form old location
[at(S, To), at(B, To)] % Place both in new location
).

%  Action: Climb Up Box
act( climbUp(B), % Any box needed
[shakey(S), box(B), on(S, floor), at(B, X), at(S, X)], % Shakey on floor, box and shakey in same room
[on(S, floor)], % Remove
[on(S, box)] % Place
).

%  Action: Climb Down Box
act( climbUp(B), % Any box needed
[shakey(S), box(B), on(S, B), at(B, X), at(S, X)],
[on(S, box)], % Remove
[on(S, floor)] % Place
).

%  Action: LightOn
act( turnOn(), % There is only one lightswitch per room, so which is implicit
[shakey(S),switch(L) ,box(B), at(S, X), at(B, X), on(S, box), lights(X, off)], %
[lights(X, off)],
[lights(X, on)]
).

%  Action: LightOff
act( turnOff(), % There is only one lightswitch per room, so which is implicit
[shakey(S), box(B), at(S, X), at(B, X), on(S, box), lights(X, on)], %
[lights(X, on)],
[lights(X, off)]
).


goal_state([
lights(light1, off),
at(box2,room2)

]).


initial_state([

% Place shakey <3
shakey(s),
at(s,room3),
on(s,floor),

% Connect all rooms
binding(room1, corridor),
binding(room2, corridor),
binding(room3, corridor),
binding(room4, corridor),
binding(room4, corridor),
binding(corridor, room1),
binding(corridor, room2),
binding(corridor, room3),
binding(corridor, room4),


% Install lightswitches in rooms
binding(room4, light4),
binding(room3, light3),
binding(room2, light2),
binding(room1, light1),
binding(light4, room4),
binding(light3, room3),
binding(light2, room2),
binding(light1, room1),

% Set light states - Doing reverse according to image
lights(light4, off),
lights(light3, on),
lights(light2, on),
lights(light1, on),

% Create boxes
box(box1),
box(box2),
box(box3),
box(box4),

% Place blocks n shit cuz this is fucking minecraft
at(box1, room1),
at(box2, room1),
at(box3, room1),
at(box4, room1)
]).
