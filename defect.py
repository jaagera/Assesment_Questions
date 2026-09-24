def passing_scores(scores):
    passed = []
    for index in range(len(scores) - 1):
        if scores[index] > 50:
            passed.append(scores[index])
    return passed

print(passing_scores([49, 50, 80, 65]))

Predicted output: [80]

#Defect 1: range(len(scores) - 1) stops one spot too early (an 
#"off-by-one" error). With a 4-item list, this only checks spots 
#0, 1, and 2, and never checks the last spot (index 3). This loses 
#the score 65, which should have passed but is never even examined.

#Defect 2: The condition scores[index] > 50 uses strictly "greater 
#than," but the requirement is "greater than or equal to" 50. This 
#means a score of exactly 50 is wrongly excluded. This loses the 
#score 50, which should have passed the boundary check.