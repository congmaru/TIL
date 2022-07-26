# #자릿수더하기
# #반복문을 사용한 버전
# def sum_number():
#     N = input('숫자를 입력하세요')
#     lN = list(N)
#     intN = []
#     for n in lN:
#         if n in '012345679':
#             n = int(n)
#             intN.append(n)
#     return sum(intN)

# print(sum_number())

# #반복문을 사용. 수정한 버전
# def sum_number(N):
#     lN = list(str(N))
#     intN = []
#     for n in lN:
#         if n in '012345679':
#             n = int(n)
#             intN.append(n)
#     return sum(intN)

# print(sum_number(1234))



# #재귀를 사용한 버전
# def sum_of_digit(N):
#     if N == 0:
#         return 0
#     else:  
#         a = N % 10
#         b = N // 10
#     return a + sum_of_digit(b)

# print(sum_of_digit(555))


#재귀로 자릿수구하기 -> 계속 10으로 나눈 나머지를 더하면 된다. 
#555 % 10 -> 5
#555 //10 -> 55
#55%10 -> 5
#55//10 -> 5

# def sum_jea(N):
#     if N == 0:  
#         return 0
#     else:
#         a = N%10
#         b = N//10
#     return a + sum_jea(b)

# print(sum_jea(555))

# #교수님풀이
# def sum_of_d(num):
#     if num <10:
#         return num
    
#     return num%10 + sum_of_d(num//10)

# print(sum_of_d(5))
# (sum_of_d(123))


# #피보나치
# def fibonacci(num):
#     if num == 0:
#         return 0
#     elif num ==1:
#         return 1

#     return fibonacci((num-1))+ fibonacci(num-2)


# def fibonacci(num):
#     if num<2:
#         return num
#     return fibonacci((num-1))+ fibonacci(num-2)
    
# print(fibonacci(17))

# fibo_list = []
# for i in range((18)):
#     fibo_list.append(fibonacci(i))
# print(fibo_list)


#하노이의 탑
def hanoi(N, start, end, other):
    if N == 1:
        print(f'{start} -> {end}')
        return

    hanoi(N-1, start, other, end)
    print(f'{start} -> {end}')
    hanoi(N-1, other, end, start)

#원판의 갯수, 시작, 도착, 서브 기둥 번호
N = 3
hanoi(2,1,2,3)