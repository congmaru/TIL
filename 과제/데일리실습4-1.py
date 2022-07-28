#데일리실습4-1. 반복문을 활용한 비밀번호 입력 예제
#맞는 비밀번호 입력할 때까지 반복하는 코드 작성. 3회이상 틀리면 반복입력 기회없이 종료됨

cnt = 1
password = 'congmaru'
while True:
    pw = input('비밀번호를 입력하세요 : ')
    if pw == password:
        print('로그인되었습니다')
        break
    if cnt >= 3:
        print('로그인 실패. 횟수초과되었습니다')
        break
    if pw != password:
        print('다시입력하세요')
        cnt+=1
