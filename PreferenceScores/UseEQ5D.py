from PreferenceScores import EQ5D as eq

print("Score for ", [1, 1, 2, 3, 1])
print(eq.get_score(mobility=1, self_care=1, usual_activity=2, pain_discomfort=3, anxiety_depression=1))

print("Score for perfect health")
print(eq.get_score(mobility=1, self_care=1, usual_activity=1, pain_discomfort=1, anxiety_depression=1))

# an unacceptable value for self-care
#print(eq.get_score(mobility=1, self_care=0, usual_activity=1, pain_discomfort=1, anxiety_depression=1))
# an unacceptable value for usual activity
#print(eq.get_score(mobility=1, self_care=1, usual_activity=5, pain_discomfort=1, anxiety_depression=1))