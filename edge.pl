edge(a,b,2).
edge(a,c,1).
edge(c,d,1).
edge(b,e,4).

best_first(Start, Goal) :-
    edge(Start, Goal, _).

best_first(Start, Goal) :-
    edge(Start, Next, _),
    best_first(Next, Goal).