#과수원에 농부 한명이 썩은 과일이 몇개 들어있는 과일 봉지를 가지고 있다.
#과일 봉지를 입력 받아, 썩은 과일 조각들을 모두 신선한 것으로 교체하는 코드를 작성하고 리스트 형식으로 출력하시오.
#예를 들어, apple,rottenBanana,apple,RoTTenorange,Orange이라는 문자열이 주어진 경우, 대체된 리스트는 ['apple', 'banana', 'apple', 'orange', 'orange'] 이어야 한다.

def func1():
    fruits = input('과일봉지안에 무엇이 들어있나요?').split(',') #
    result_list = []
    for fruit in fruits:
        fruit = fruit.lower()
        if  fruit[:6] =='rotten':
            fruit = fruit[6:]
        result_list.append(fruit)
    print(result_list) #리스트업

func1()

def func2():
    fruits = input('과일을 입력하세요 : ').split((','))
    result_list = []
    for fruit in fruits:
        fruit = fruit.lower()
        if fruit[:6] == 'rotten':    #[:6] = 0~5까지/ [1:3] = 1에서 2까지
            fruit = fruit[6:]
        result_list.append(fruit)
    print(result_list)

func2()


# result_list.append(fruit)
#         a= set(result_list)이렇게 바꾸면 중복된걸 바꿀 수 있다.





