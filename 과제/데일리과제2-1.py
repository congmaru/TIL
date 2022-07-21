#데일리과제 2-1
orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'
orders_list = orders.split(',')
print(orders_list)

#1. 주문개수세기
print(len(orders_list))

#2. 내림차순정렬
orders_list.sort(reverse=True)  #그 자리에서 저장할 때 사용
# new_list = sorted(orders_list) #새로운데 저장할 때 사용
print(orders_list)
    
#3. 중복제거 -> set 이용
print(set(orders_list))


#4. 아이스음료 주문은 몇개인가?
ice_count = 0
for order in orders_list :  #orders로 검색하면 아 이 스 이렇게 한글자씩 검색하는 걸로 나와 답이 0이 나온다. 때문에 리스트화 시켜서 뭉텅이로 검색해야함.
    if '아이스' in order:
        ice_count += 1
print(ice_count)

#5. 메뉴별 주문수를 출력하세요
order_dict={}
for order in orders_list:
    if order in order_dict:
        order_dict[order] += 1
    else:
        order_dict[order] = 1
print(order_dict)

