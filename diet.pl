diet(diabetes, 'Avoid sugar and eat vegetables').
diet(bp, 'Reduce salt intake').
diet(obesity, 'Low calorie diet').

suggest(Disease, Diet) :-
    diet(Disease, Diet).