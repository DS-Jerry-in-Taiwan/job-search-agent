raw_scores = {'skill_match': 60, 'experience_match': 80, 'preference_match': 60}
weights = {'skill': 0.5, 'experience': 0.3, 'preference': 0.2}
final_score = (
    raw_scores['skill_match'] * weights['skill'] +
    raw_scores['experience_match'] * weights['experience'] +
    raw_scores['preference_match'] * weights['preference']
) / 100
print(f"final_score = {final_score:.2f}")
