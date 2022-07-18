#데일리실습 1-3

SSN = input('주민번호를 입력하세요(123456-1234567): ')

result = SSN.split('-')

if len(result[0]) >= 7 or len(result[1]) >= 8:
    print('잘못입력했습니다')
else: 
    print(result[0]+'*******')
