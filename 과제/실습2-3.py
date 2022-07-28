#하나의 문장이 주어졌을 때, 그 문장을 끝말잇기로 보기로 하였다.
#세 단어가 입력으로 주어졌을 때 그 끝말잇기가 옳으면 Pass, 옳지 않으면 Fail을 출력하시오.
#예를 들어 saFe eMotion Nail 인 경우, pass를 출력한다.

sentence = input('문장을 입력하세요')
sentenc = sentence.lower()
senten = sentenc.split(' ')
if senten[0][-1] == senten[1][0]:
    if senten[1][-1] == senten[2][0]:
        print('pass!')
    else :
        print('fail')
else :
    print('fail')

# for i in range(len(senten)):
#     if senten[i-1][-1] == senten[i][0]:
#         # if i==0:
#         #     continue
#         print('pass')
    
#     else:
#         print('fail')
    