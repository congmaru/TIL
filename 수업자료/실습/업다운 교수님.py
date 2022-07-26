import random

is_playing = True

while is_playing:
    print('================================')
    print('        Up and Down Game        ')
    print('================================')

    answer = random.randint(1, 10000)  # 1이상 10000이하의 난수
    counts = 0  # 몇 번만에 정답을 맞혔는지 담는 변수

    # 여기부터 코드를 작성하세요.
    while True:
        if number < 1 or number > 10000:
            print('다시입력하세요')
            continue

        #2. 정답 맞히기
        counts += 1

        #2-1. 사용자의 숫자와 정답을 비교하기
        if number < answer:
            print('up')
        elif number > answer:
            print('down')

        #2-2.
        else:
            print(f'정답입니다 {counts}회 만에 정답을 맞히셨습니다')
            break

    #3. 게임 재시작 여부 판단
    user_choice = input('게임을 재시작 하려면 y, 종료하시려면 n을 입력하세요 : ')

    #3-1. y입력시 재시작
    if user_choice == 'y':
        continue

    #3-2. n 입력시 종료
    #3-3. n외의 문자는 종료
    if user_choice == 'n':
        print('이용해주셔서 감사합니다. 게임을 종료합니다.')
    else:
        print('잘못입력햇습니다. 게임을 종료합니다.')

    
    

