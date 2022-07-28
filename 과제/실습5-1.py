#과일봉지 입력받아, 썩은건 모두 신선한 것으로 교체하고 리스트 형식으로 출력하는 함수를 만들어라.
fruits = ['apple','rottenBanana','apple','RoTTenorange','Orange']



def new_fruits(fruits):
    fl_lst = []
    for f in fruits:
        fl_lst.append(f.lower())
    
    new_lst = []
    for fruit in fl_lst:
        if fruit[0:6] == 'rotten':
            new_lst.append(fruit[6:])
        else:
            new_lst.append(fruit)
    return new_lst


print(new_fruits(fruits))


