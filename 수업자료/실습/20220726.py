# #실습 python05. 데이터 구조 및 활용
# #problem1
# def count_vowels():
#     Sen = input(('문자열을 입력하세요'))
#     sen = Sen.lower()
#     lst = list(sen)
#     print(lst)
#     vowel = ['a','e','i','o','u']
#     cnt = 0
#     for i in vowel:
#         cnt+= sen.count(i)
#     return cnt

# print(count_vowels())

# def count_vowels(words):
#     # count = 0
#     # count += words.count('a')
#     # count += words.count('e')
#     # count += words.count('i')
#     # count += words.count('o')
#     # count += words.count('u')
#     # return count
#     vowels = 'aeiou'
#     count = 0
#     for vowel in vowels:
#         count += words.count(vowel)
#     return count

# print(count_vowels('apple'))

# #problem2

# #problem3 완전탐색 : 전체데이터를 순회하면서 다 체크하는것
# def only_square_area(widths, heights):
#     combination_list = []
#     for width in widths:
#         for height in heights:
#             if width == height:
#                 combination_list.append(width*height)
#     return combination_list

# print(only_square_area([32, 55, 63], [13, 32, 40, 55]))
 
# def only_square_area(widths, heights):
#     combination_list = []
#     for width in widths:
#         if width in heights:
#             combination_list.append(width**2)
#     return combination_list

# print(only_square_area([32, 55, 63], [13, 32, 40, 55]))

# print('apple'.strip())


# def duplicated_letters(N):
#     lN = list(N)
#     for i in lN:
#         if i == lN:
#             .append()


    
# #교수님 풀이 #중복여부 가리는 코드. 한번더 추가방지
#무엇이 중복일까
#문자열을 전달 받아 해당 문자열에서 중복해서 나타난 문자들을 담은 list를 반환하는 duplicated_letters 함수를 작성하시오
# def duplicated_letters(words):
#     duplicates = []
#     for word in words:
#         if words.count(word) > 1 and word not in duplicates: 
#             duplicates.append(word)
#     return duplicates

# print(duplicated_letters('apple'))

# def duplicated_letters(words):
#     return list({word for word in words if words.count(word)>1})

# print(duplicated_letters('apple'))

#소대소대
#문자열을 전달 받아 해당 문자열을 소문자와 대문자가 번갈아 나타나도록 변환하여 반환하는 low_and_up 함수를 작성하시오. 
#이때, 전달 받는 문자열은 알파벳으로만 구성된다

# def low_and_up(word):
#     new_str =''
#     for idx, char in enumerate(word):
#         if idx %2 == 1:
#             new_str += char.upper()
#         else:
#             new_str += char.lower()
#     return new_str

# print(low_and_up('apple'))


def low_and_up2(word):
    new_str = [(char.upper() if idx%2 else char.lower()) for idx, char in enumerate(word)]
    return ''.join(new_str)

print(low_and_up2('apple'))