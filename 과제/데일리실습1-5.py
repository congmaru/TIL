#데일리실습1-5
# def func2():
#     wide = int(input())
#     height = int(input())
    
#     for _ in range(height):
#         for _ in range(wide):
#             print('*', end ='')
#         print()

# func2()
    


# def func3():

#     wide = int(input())
#     height = int(input())

#     for _ in range(height):
#         print('*' * wide)

# func3()



# def func4():

#     wide = int(input('가로'))
#     height = int(input('세로'))

#     tup = (wide, height)

#     for _ in range(tup[1]):
        
#         print('*' * tup[0])

# func4()

s_triangle = list(map(int,input('세 변의 길이를 입력하시오. : ').split()))
s_triangle = sorted(s_triangle)

if s_triangle[0] + s_triangle[1] <= s_triangle[2]:
    print('삼각형 아님')
elif s_triangle[0] == s_triangle[1] == s_triangle[2]:
    print('정삼각형')
elif s_triangle[0] == s_triangle[1] or s_triangle[1] == s_triangle[2]:
    print('이등변삼각형')
elif s_triangle[0] ** 2 + s_triangle[1] ** 2 == s_triangle[2] ** 2:
    print('직각삼각형')
else :
    print('삼각형')