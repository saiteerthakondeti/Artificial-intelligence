bird(sparrow).
bird(parrot).
bird(penguin).

can_fly(sparrow).
can_fly(parrot).

cannot_fly(X) :-
    bird(X),
    \+ can_fly(X).