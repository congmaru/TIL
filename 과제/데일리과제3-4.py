#데일리과제 3-4
#문자열 s-trial로 각 변을 입력받았을 때 어떤 삼각형인지 출력한다.

s_triangle = list(map(int,input('삼각형의 세 변을 띄어쓰기로 입력하세요').split()))
st = sorted(s_triangle,reverse=True)

if st[0] >= st[1]+st[2]:
    print('삼각형이 아닙니다.')
else: 
    if st[0] == st[1] == st[2]:
        print('정삼각형입니다')
    elif st[0] == st[1] or st[0] == st[2] or st[1] == st[2]:
        print('이등변삼각형입니다')
    elif st[2]**2 == st[0] **2 + st[1] **2:
        print('직각삼각형입니다')



# s_triangle = list(map(int,input('세 변의 길이를 입력하시오. : ').split()))
# s_triangle = sorted(s_triangle)

# if s_triangle[0] == s_triangle[1] == s_triangle[2]:
#     print('정삼각형')
# elif s_triangle[0] == s_triangle[1] or s_triangle[1] == s_triangle[2]:
#     print('이등변삼각형')
# elif s_triangle[0] ** 2 + s_triangle[1] ** 2 == s_triangle[2] ** 2:
#     print('직각삼각형')
# elif s_triangle[0] + s_triangle[1] > s_triangle[2]:
#     print('삼각형')
# else:
#     print('삼각형 아님')

# s_triangle = list(map(int,input('세 변의 길이를 입력하시오. : ').split()))
# s_triangle = sorted(s_triangle)

# if s_triangle[0] == s_triangle[1] == s_triangle[2]:
#     print('정삼각형')
# elif s_triangle[0] == s_triangle[1] or s_triangle[1] == s_triangle[2]:
#     print('이등변삼각형')
# elif s_triangle[0] ** 2 + s_triangle[1] ** 2 == s_triangle[2] ** 2:
#     print('직각삼각형')
# elif s_triangle[0] + s_triangle[1] > s_triangle[2]:
#     print('삼각형')
# else:
#     print('삼각형 아님')