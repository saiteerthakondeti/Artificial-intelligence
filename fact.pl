fact(a).
fact(b).

rule(c) :- fact(a), fact(b).
rule(d) :- rule(c).

forward(X) :-
    rule(X).