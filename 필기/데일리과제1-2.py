##데일리과제 1-2


#김해피성적
score = {'python': 80, 'django': 89, 'web': 83}
print(score)

#알고리즘성적추가
score['algorithm'] = 90
print(score)

#성적수정
score['python'] = 85
print(score)

#과목평균출력
sum_score = sum(score.values(  ))
print(sum_score/4) 

#다른방법
print(sum_score/len(score))
