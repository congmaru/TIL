#몇잔의 주문이 들어왔는지 확인
#중복을 제거한 메뉴만을 리스트 형식으로 출력(단, 내림차순정렬)

def func1():
    orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'
    orders_list = orders.split((','))
    # print(orders_list)
    #1. 주문개수세기
    print(len(orders_list))

    #2. 내림차순정렬
    new_list = orders_list
    
    #3. 중복제거 -> set 이용
    


func1()
