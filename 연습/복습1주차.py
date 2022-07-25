#부동소수점
a = 3.2-3.1 #0.10000000000000009
b = 1.2-1.1 #0.09999999999999987
#실제론 0.1이 나와야 하나 컴퓨터와 사람이 사용하는 숫자체계 달라 다르게 나옴
print(a,b)

import math
from os import lstat
print(math.isclose(a,b)) 
#math함수를 이용해 a,b가 근사한지 값 비교할 수 있다. 

#삼중따옴표 : 이 안에 있는건 모조리 문자열이 된다.
print('''문자열 안에 '작은따옴표'나
"큰따옴표"를 사용할수도 있고
여러줄을 사용하 때에도 편리하다.''')

print('''철수 \n 안녕\t''')


#문자열을 변수로 활용하는법 f-format
name = 'kim'
score = 4.5

print('Hi my name %s, score %s' % (name, score))
print('내 성적은 %f' % score)
print('%d' %score)

print('Hi, {}!, my score is {}'.format(name, score))

print(f'hi my name is {name}, score{score}')


print(True and True)
print(True and False)
print(False and True)
print(False and False)
print(True or True)
print(True or False)
print(False or True)
print(False or False)

##23시가 되었고, 잠이 오는 경우
hour = 20
status = 'sleepy'
if hour >= 23:
    print(status)
else:
    print('not', status)

#논리연산자 단축평가
print(3 and 5)
print(3 and 0)
print(0 and 3)
print(0 and 0)
print(3 or 5)
print(3 or 0)
print(0 or 3)
print(0 or 0)


#리스트 : 순서O. 자료변경 가능
location = ['서울', '광주', '대구', '부산']
print(location[-1])
location[0] = '제주도'
print(location)
print(len(location))
print(location[-1][0])

#튜플 : 순서O. 자료변경 불가능
a = (1,2,3,1)
print(a[1])
# a[1]= 598
# print(a)

x, y = 1, 2
print(x, y)

#레인지 : 순서O. 자료변경 불가능. 주로 반복문과 함께 사용
print(list(range(2,5)))
print(list(range(2, 10, 3)))
print(list(range(10,1,2)))

#슬라이싱
print([1,2,3,4][1:4])
print([1,2,3,4][3:])
print([1,2,3,4][:3])
print([1,2,3,4][0:4:2])
print((1,2,3,4,5,)[1:4:2])

s = 'abcdefghi'
print(s[2:5]) 
print(s[2:5:2])
print(s[5:2:-1])
print(s[:3])
print(s[5:])
print(s[::])
print(s[::-1])

#셋
num = {1,2,3,2,4,1,4}
print(num)
print(type(num))

blank = {}
blank_set = set()
print(type(blank))
print(type(blank_set))

#아래의 리스트에서 고유한 지역을 순서대로 출력하시오
lst = ['서울', '대전', '대구', '부산', '광주', '순천', '서울', '광주']
s_lst = set(lst)
ss_lst = sorted(s_lst)
print(s_lst, ss_lst)

a = sorted(lst)
b = sorted(lst, reverse=True)
print(a)
print(b)

#딕셔너리
dict_a = {}
dict_a = {'apple'}
dict_b = {'apple':'abc'}
print(type(dict_b))

# dic_a = {'a': 'apple', 'b:'}

##제어문
#조건문
# a = 6
# if a>5:
#     print('5초과')
# else :
#     print('5이하')


# num = int(input('숫자를 입력하세요'))
# if num % 2 ==0 :
#     print('짝수입니다')
# else:
#     print('홀수입니다')


dust = -500
if dust > 150:
    print('매우나쁨')
elif dust > 80:
    print('나쁨')
elif dust >30:
    print('보통')
elif dust >0:
    print('좋음')
else:
    print('잘못입력하셨습니다')

num = 2
result = '홀수입니다' if num %2 else  '짝수입니다'
print(result)

num = -5
value = num if num>0 else 0
print(value)

if num > 0:
    value = num
else:
    value = 0
print(value)


a = 0
while a<5:
    print(a)
    a += 1
print('끝')

fruits = ['apple', 'banana', 'mange']
for fruit in fruits:
    print(fruit)

#사용자가 입력한 문자를 한글자씩 출력하시오
# chars = input('단어를 입력하세요')
# for char in chars:
#     print(char)

#사용자가 입력한 문자를 range를 활용하여 한글자씩 출력하시오
# chars = input('단어를 입력하시오')
# for i in range(len(chars)):
#     print(chars[i])


#딕셔너리 순회
s_lst = {'john':80, 'tim': 90}
for student in s_lst:
    print(student)  #john, tim. 기본적으로 key가 순회되고 있음
print(s_lst['john']) #80. 딕셔너리의 값 추출
for student in s_lst:
    print(student, s_lst[student]) # john 80. 키와 키의 값을 추출하는 것. 
print(s_lst.keys())
print(s_lst.values())
print(s_lst.items())
for student, grade in s_lst.items():
    print(student, grade)


#enumerate 순회
members = ['철수', '영희', '순희']
for idx, name in enumerate(members):
    print(idx, name)
a = list(enumerate(members, start=1))
print(a)

seasons = ['spring', 'summer']
a= list(enumerate(seasons, start = 1))
print(a)

#딕셔너리 실습
#1~3 세제곱 결과가 담긴 딕셔너리를 만드세요
n_dict = {}
for number in range(1,4):
    n_dict[number] = number**3
print(n_dict)

#제어문
n=0
while True:
    if n==3:
        break
    print(n)
    n+=1

for i in range(10):
    if i>1:
        print('0과1만필요하다고')
        break
    print(i)

for i in range(6):
    if i %2 == 0:
        continue
    print(i)


for char in 'apple':
    if char == 'b':
        print('야호')
        break
else:
    print('어? b가없어')


def func(x,y):
    return x*y

func(4,5)
ans = func(4,5)
print(ans)


#튜플을 사용하여 두개 이상의 값 반환할 수 있다.
def func1(x, y):
    return x-y, x*y

y = func1(4,5)
print(y)

#똑바로 읽어도 거꾸로 읽어도 같은 단어를 찾는 함수
word_list = ['우영우', '기러기', '파이썬', '별똥별']
def func3(word_list):
    real_list = []
    for word in word_list:
        if word == word[::-1]:
            real_list.append(word)
    return real_list
print(func3(word_list))

