#실습 1-2.
# a = int(input('게시글의 총 개수를 입력하세요'))
# b = int(input('한 페이지에 필요한 게시글 수를 입력하세요'))
# c = int(a/b)
# if float(a/b) > c:
#     c = c+1
#     print(c)
# else:
#     print(int(c))


#실습 1-3
# SSN = input('주민번호 13자리를 -를 이용해 입력하세요')
# print(SSN[0:6]+'*******')

#실습 1-4
# lst=[]
# for i in range(1000):
#     if i %2 == 0 or i%7 == 0:
#         lst.append(i)
# print(sum(lst))

#실습1-5
# n= int(input('정수를 입력하세요'))
# m= int(input('정수를 입력하세요'))

# for i in range(n):
#     print('*'*m)

# #과제 1-2
# score = {'python':80, 'django':89, 'web':83}
# score['algorithm'] = 90
# print(score)
# score['python'] = 85
# print(score)
# lst = []
# for i in score:
#     lst.append(score[i])
# print(sum(lst)/len(lst))  #야호 성공했숴!!!!!!!


#과제 1-4. 자릿수출력
# s = input('숫자를 입력하세요')
# s_list = list(s)
# result = 0
# for i in s_list:
#     result = result + int(i)
# print(result)

# #실습2-2
# #모든 대문자는 소문자로. 가장 첫번째 대문자는 그대로 유지
# #문자열 앞뒤의 특수문자 삭제

# chars = '@#~I NeVEr DrEamEd AbouT SuCCeSs, i woRkEd foR iT.!>!'
# a = chars.upper()
# b = a.strip('@#~!>')  #a.strip(여기있는거 제거 공백'', 특수문자'@#!$')
# c = b.capitalize()
# print(c)

# #실습2-1. 근의공식 전환
# a = 3
# b = 6
# c = -5

# x1 = (-b + (b*b - 4*a*c)**(1/2))/(2*a)
# x2 = (-b - (b*b - 4*a*c)**(1/2))/(2*a)

# print('%0.4f' % x1, '%0.4f' % x2)

# #실습 2-3.
# s = input('세 단어로 된 문장을 입력하세요')
# s_l = s.lower()
# i = s_l.split(' ')
# if i[0][-1] == i[1][0]:
#     if i[1][-1] == i[2][0]:
#         print('pass!')
#     else:
#         print('fail')
# else:
#     print('fail')

##데일리실습 2-4
# steak = float(input('스테이크의 가격을 입력하세요'))
# vat = steak *0.15
# total = steak + vat

# print('스테이크', steak)
# print('+ VAT', vat)
# print('총계 W', total)

# #데일리실습 2-5 한번더!
# #작물과 가격이 함께 있는 리스트가 존재할 때, 가장 높은 가격을 가지고 있는 작물의 이름을 출력하라.
# #단, 작물의 이름을 직접 입력하여 출력하지 않는다
# crops = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]
# lst_n = []
# lst_p = []
# for i in crops:
#     lst_n.append(i[0])
#     lst_p.append(i[1])
# print(lst_n, lst_p)

# max_p = max(lst_p)  #lst_p에서의 맥스값 찾기
# index_p = lst_p.index(max_p) #lst_p에서 맥스값의 위치찾기
# print(lst_n[index_p]) #lst_n에서 맥스값위치를 넣어서 이름 찾기



# #데일리과제2-2

# orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'
# order = orders.split(',')

# # #1. 총 몇잔의 주문이 들어왔나?
# # print(len(order))

# #2. 중복을 제거하고 리스트형식으로 출력. 단 내림차순
# a = set(order) #중복제거
# b = list(a) #리스트화
# c = b.sort(reverse=True)
# print(c)
# b.sort(reverse=True)
# print(b)
# c = sorted(b, reverse=True) #sorted는 새로운 것을 반환해주는데, sort는 반환하지 않고 정렬하는 것이라 none이 나온다.
# print(c)

# #3. 아이스 음료 주문이 몇개 들어왔는지 확인
# cnt_ice = 0
# for i in order:
#     if i[0:3] == '아이스':
#         cnt_ice += 1
#     else :
#         pass
# print(cnt_ice)

# #4. 메뉴별 주문수를 출력하세요
# m_dict = {}
# for i in order:
#     if i in m_dict:
#         m_dict[i] += 1
#     else:
#         m_dict[i] = 1
# print(m_dict)

# #데일리실습 3-1
# fruits = input('과일봉지안에 무엇이 들어있나요?').split(',')
# result_list = []
# for fruit in fruits:
#     fruit = fruit.lower()
#     if  fruit[:6] =='rotten':
#         fruit = fruit[6:]
#     result_list.append(fruit)
# print(result_list) 

# #데일리실습 3-2
# #문자열을 전달받아 해당 문자열의 정중앙 문자를 출력하시오.
# #짝수일 경우에는 정중앙 문자 2개를 출력하라.
# word = input('단어를 입력하세요')
# if len(word) % 2 == 1:
#     index = len(word)//2
#     print(word[index])
# else:
#     index1 = len(word)//2-1
#     index2 = len(word)//2
#     print(word[index1], word[index2])


# #데일리실습 3-3
# infos = [{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}]
# lst=[]
# for i in infos:
#     lst.append(i['age'])
# sum_lst = sum(lst)
# print(sum_lst)

# #데일리실습 3-4
# #여러 사람의 혈액형(A, B, AB, O)에 대한 정보가 담긴 list를 전달 받아, key는 혈액형의 종류, value는 사람 수인 dictionary를 만드시오.
blood_types = [ 'A','A','O', 'B', 'A', 'O', 'AB','O', 'A', 'B', 'O', 'B', 'AB']
# b_dict={'A':0,
#         'B':0,
#         'AB':0,
#         'O' :0}
# for i in blood_types:
#     b_dict[i] += 1
# print(b_dict)

b_dict = {
    'A' : 0,
    'B' : 0,
    'AB' : 0,
    "O" : 0
}
for i in blood_types:
    b_dict[i] += 1
print(b_dict
    )

#데일리 실습 3-5


#데일리과제 3-2 윤년 판별하기

# year = int(input('윤년인지 알고싶은 해를 입력하세요'))
# if year % 4 == 0 and year %100 != 0:
#     print('윤년입니다')
# elif year % 400 == 0:
#     print('윤년입니다')
# else:
#     print('윤년이아니네요')

#데일리과제 3-4
#문자열 s-trial로 각 변을 입력받았을 때 어떤 삼각형인지 출력한다.

# s_triangle = int(input('삼각형의 세 변을 띄어쓰기로 입력하세요').split(' '))

#데일리실습 4-1
# password = 'congmaru'
# while True:
#     pw = input('비밀번호를 입력하세요')
#     cnt_pw = 0
#     if pw == password:
#         print('로그인 되었습니다')
#         break
    
# if pw != password:
#         cnt_pw += 1
#         print('다시입력해주세요')
#         continue
#     if cnt_pw >=3:
#         print('종료됩니다')
#         break
