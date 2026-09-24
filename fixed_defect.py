def passing_scores(scores):
    passed = []
    for index in range(len(scores)):
        if scores[index] >= 50:
            passed.append(scores[index])
    return passed

print(passing_scores([49, 50, 80, 65]))

#All three qualifying scores are now included, and the order is kept the same as in the original list. 🎯