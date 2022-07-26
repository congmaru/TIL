import random

is_playing = True

while is_playing:
    print('================================')
    print('        Up and Down Game        ')
    print('================================')

    answer = random.randint(1, 10000)  # 1이상 10000이하의 난수
    counts = 0  # 몇 번만에 정답을 맞혔는지 담는 변수

    # 여기부터 코드를 작성하세요.

    while Ture:
        n = int(input('1이상 10000이하의 숫자를 입력하세요'))
        counts += 1
        if(n<0 or n>10000):
            print('잘못된 범위의 숫자를 입력하셨습니다. 다시 입력해주세요')
            # continue
        elif n>answer:
            print('down!')
        elif n<answer:
            print('up!')
        elif n == answer:
            print('correct!! {}회 만에 정답을 맞히셨습니다.'.format(counts))
            break

s="게임을 재시작 하려면 y, 종료하시려면 n을 입력하세요 : "
choice = input(s)
if choice == 'y':
    continue
elif choice == 'n':
    print('이용해주셔서 감사합니다. 게임을 종료합니다.')
    break
else:
    print('잘못된 값을 입력하셨습니다. 게임을 종료합니다')
    break
