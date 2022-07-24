#하나의 문장이 주어졌을 때, 그 문장을 끝말잇기로 보기로 하였다.
#세 단어가 입력으로 주어졌을 때 그 끝말잇기가 옳으면 Pass, 옳지 않으면 Fail을 출력하시오.
#예를 들어 saFe eMotion Nail 인 경우, pass를 출력한다.

s = input('문장을 입력하세요')
result = s.split(' ')
lst_result = list(result)

if 