#데일리실습 4-3
#정수 0부터 9까지로 이루어진 list를 전달 받아, 연속적으로 나타나는 숫자는 하나만 남기고 제거한 list를 출력하라.
# 이때, 제거된 후 남은 수들이 담긴 list의 요소들은 기존의 순서를 유지해야 한다.

# def func1():
#     lst = input('0부터 9까지의 정수를 입력하세요').split(',') #결과가 lst이므로 int처리 불가@!
#     print(list(set(lst)))
# func1()  #이렇게 했을 때 순서가 유지되지 않음.

def func2():
    lst = input('0부터 9까지의 정수를 띄어쓰기하여 무작위로 입력하세요').split(' ')
    print(dict.fromkeys(lst))
    print(list(dict.fromkeys(lst)))
    

func2()

#dictionary는 key값을 넣는 순서를 기억하므로, list(dict.fromkeys(lst))를 사용하면 된다.