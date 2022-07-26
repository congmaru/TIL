print('=================================')
print('         Vending Machine         ')
print('=================================')
print('[Menu]')
print('1. 콜라 500원')
print('2. 사이다 700원')
print('3. 레모네이드 4500원')
print('4. 오렌지주스 2000원')
print('5. 초코우유 1200원')
print('6. 아메리카노 3600원')
print('=================================')

menus = ['콜라', '사이다', '레모네이드', '오렌지주스', '초코우유', '아메리카노']  # 메뉴 이름
costs = [500, 700, 4500, 2000, 1200, 3600]  # 메뉴 가격
budget = 0  # 자판기에 넣은 총 누적 금액


while True:
    print()
    money = int(input('금액을 넣어주세요.(그만 넣으시려면 0을 입력하세요.) : '))

    # 여기부터 코드를 작성하세요.
    
    if(money < 0):
        print('금액은 1원 이상 넣어주세요')
    elif(money >0):
        budget += money 
        print('현재 누적된 금액은', budget, '원 입니다')
    else:
        break




if(budget < costs[0]):
    print(budget,'원으로 구매가능한 메뉴가 없습니다')
else:
    print(budget,'원으로 구매가능한 메뉴는 다음과 같습니다')
    if cost[i] <= budget:
        print(f'{i+1}. {menus[i]} {costs[i]}원')

    # for i in range (0,6):
        # print(f"{i+1}. {menus[i]} {costs[i]}")  #영식님헬프감사링

    
# while True:
#     try:
#         choice = int(input('구매하실 메뉴의 번호를 입력하세요 : '))
