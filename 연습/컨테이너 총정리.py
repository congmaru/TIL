#시퀀스 : 순서O -> indexing, slicing 가능
#list, tuple, range

##list : [], list(). 가변 mutable.
# def func1():
#     lst=['a', 'b']
#     print(lst[0]) #a #위치
#     # lst[2] = 'c' #이렇게 추가가 안되네
#     lst.append('c') #.append() : 리스트 맨 마지막에 요소가 추가 ['a', 'b', 'c']
#     print(lst)
#     lst.insert(0, 123) #.insert(index, value): 지정된 위치에 요소 추가 [123, 'a', 'b', 'c']
#     print(lst)
#     lst.remove('b') #.remove(value) : 지정된 값 삭제 [123, 'a', 'c']
#     print(lst)
    

# func1()

##tuple : (), tuple(). 불변 immutable.
# def func2():
#     tup=('a','b','c',)
#     print(tup)
#     print(tup[1])  #b 위치

#     x, y = 1, 2
#     print(x, y)  #우변이 곧 좌변

# func2()


#비시퀀스
#set :  {}, set(). 중복된 값 쉽게 제거가능. mutable

# def func3():
#     a = {1, 2, 2, 3, 3, 4, 4, 4, 1, 6}
#     print(set(a)) #{1, 2, 3, 4, 6} 중복된 값 제거됨

# func3()

#dictionary : {}, dict(). {'key' : value}형식으로 이루어짐. 이 때 key는 immutable한 str, tup, range, str, float 등이 사용가능.

# def func4():
#     dict_a={}  #set과 똑같이 {}를 쓰지만 속이 빈 {}라면 무조건 dict. mutable
#     dict_b={'a':1, 'b':2, 'c':[1,2,3]}
#     print(dict_b['b']) #key값을 집어넣어야한다.

# func4()

# def func5():
#     num = 2
#     if num %2 == 0:
#         result = '짝수입니다'
#     else:
#         result = '홀수입니다'
#     print(result)
# func5()

# def func6():
#     num = 2
#     result = '짝수입니다' if num %2 == 0 else '홀수입니다'
#     print(result)
# func6()

from signal import signal


def func7():
    grades = {'john' : 80, 'eric' : 90}
    for i in grades:
        print(i, grades[i])

func7()

