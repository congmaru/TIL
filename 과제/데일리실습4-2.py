students = ['박해피', '이영희', '조민지', '조민지', 
            '김철수', '이영희', '이영희', '김해킹',
            '박해피', '김철수', '한케이', '강디티',
            '조민지', '박해피', '김철수', '이영희',
            '박해피', '김해킹', '박해피', '한케이','강디티']

vote_cnt = {}

for student in students:
    if student not in vote_cnt:
        vote_cnt[student] = 1
    else:
        vote_cnt[student] += 1

print(vote_cnt)