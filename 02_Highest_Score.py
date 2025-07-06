ans = int(input('Enter number of Subjects : '))

score_list = []
print(type(score_list))
for i in range(0,ans):
    score = int(input (f'Enter score for Subject {i+1} : '))
    score_list.append(score)

print("Scores : ", score_list)

min_score = min(score_list)
max_score = max(score_list)
avg_score = sum(score_list)/len(score_list)

print(f'Lowest Score : {min_score}' )
print(f'Highest Score : {max_score}' )
print(f'Avg Score : {avg_score}' )
