#if else문 실습
# def func1():
#     num = int(input('숫자를 입력하세요'))  #문자열이므로 int가 필요하다!
#     if num % 2 == 1:
#         print('홀수입니다')
#     else:
#         print('짝수입니다')


# func1()


#복수 조건문 실습문제. 미세먼지 농도에 따라 등급을 출력하는 조건식
# def func2():
#     dust = 100 #제시된 데이터
#     if dust > 150:
#         print('매우나쁨')  #위에서부터 실행하기 때문에 위의 조건을 만조한다면 바로 결론으로 넘어간다.
#         if dust > 300:
#             print('실외활동을 자제하세요')
#     elif dust > 80:
#         print('나쁨')
#     elif dust > 30:
#         print('보통')
#     elif dust >= 0:
#         print('좋음')
#     else:
#         print('값이 잘못되었습니다')
#     print('미세먼지 확인 완료!')

# func2()

# def func3():
#     num = -5
#     if num>= 0:
#         value = num
#     else :
#         value = 0
#     print(value)

# func3()

#while문 실습
# def func4():
#     a = 0
#     while a < 5:
#         print(a)
#         a += 1
#     print('끝')

# func4()

#for문 실습
# def func5():
#     fruits = ['apple', 'mange', 'banana']
#     for fruit in fruits:
#         print(fruit)
#     print('끝')

# func5()

# def func6():
#     chars = input('happy')
#     for char in chars:
#         print(char)

# func6()


#딕셔너리
# def func7():
#     grades = {'john' : 80, 'eric' : 90}
#     for student in grades:
#         print(student)
    
#     for student in grades:
#         print(student, grades[student])

#     print(grades.keys())
#     print(grades.values())
#     print(grades.items())

#     for student, grade in grades.items():
#         print(student, grades)

# func7()

    

#함수 실행 예시
# def func8():
#     num1 = 0
#     num2 = 1

#     def func_1(a,b):
#         return a+b
#     def func_2(a,b):
#         return a-b
#     def func_3(a,b):
#         return func_1(a,5) + func_2(5,b)
    
#     result = func_3(num1,num2)    #func_1과 2는 실행되니 않고 3만 실행
#     print(result)

# func8()


#Webex실습 1. 세로로 출력하기
#자연수 number를 입력받아, 1부터 number까지의 수를 세로로 한줄씩 출력하시오
# def func_a():
#     num = int(input('자연수를 입력하세요'))
#     for i in range(1,num +1):  #1부터 num까지니까 +1
#         print(i)   #세로로 출력이 기본. 가로로출력하려면 print(i, end = ' ')

# func_a()

#실습2. 자연수 number를 입력받아, number부터 0까지의 수를 세로로 한줄씩 출력하시오
# def func_b():
#     num = int(input('자연수를 입력하시오'))
#     for i in range(num, -1, -1):
#         print(i) #세로로 출력이 기본. 가로로출력하려면 print(i, end = ' ')

# func_b()  #코드짰다. 뿌드읏

#실습3.N줄 덧셈. 자연수 number를 입력받아, 1부터 주어진 자연수 number까지를 모두 더한값을 출력하시오
#단 주어지는 숫자는 10,000을 넘지 않는다.

# def func_c():
#     number = int(input('자연수를 입력하시오')) #이미 문제에 주어지는 숫자어쩌구의 조건이 주어져서 따로 코드를 짜지않아도 된다
#     # for i in range(1, number):
#     #     print(sum(number)) ##썸은 이미 내장된 함수이므로 쓰지말아라
#     result = 0
#     for i in range(1, number+1):
#         result += number
#     print(result)

    
# func_c()

#실습 3-2. 홀수만 더해봐라
# def func_d():
#     number = int(input('자연수를 입력하시오'))
#     result = 0
#     for num in range(1, number+1):
#         if num % 2 == 1:
#             result += num
#     # for i in range(1, number+1, 2):  #이렇게 코드를 짜면 결국 for로 반복되어 전체숫자의 합이 나온다.
#     #     result += number
#     #     if result = number:
#     #         break
#     print(result)
    
# func_d()



#LEGB 예시
# def func20():
#     a = 0
#     b = 1
#     def enclosed():
#         a = 10
#         c = 3
#         def local(c):
#             print(a,b,c)
#         local(300)
#         print(a, b, c)
#     enclosed()
#     print(a, b)

# func20():
# input_list = list(map(int, input().split())) #12345
# print(input_list)  #[12345]
#
# func20()

#숫자를 입력받아 1~n 더하는 함수를 재귀로 구현해라
# def func21():
#     def re(n) : 
#         if n == 1:
#             return 1
#         return n+re(n-1)
#     print(re(n))

# func21()

#위와 동일. 강사님 풀이
# def func22():
#     n = int(input('숫자입력 : '))

#     def sum_func(n) :
#         if n == 0:
#             return 0
#         return n + sum_func(n-1)
#     print(sum_func(n))

# func22()


#코딩테스트 단골문제 : 피보나치. 하노이의 탑. 최소 공배수 -> 검색해보기


#import module

