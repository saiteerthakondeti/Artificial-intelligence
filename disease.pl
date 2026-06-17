disease(fever, flu).
disease(cough, cold).
disease(headache, migraine).

diagnose(Symptom, Disease) :-
    disease(Symptom, Disease).