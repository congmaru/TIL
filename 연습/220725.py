
# word = 'ssafy'
# print(word) #ssafy
# print(id(word)) #메모리 주소 확인 3055024312624
# word = 'test'
# print(word) #test
# print(id(word)) #메모리 주소 확인 3055024334576

# print('apple'.find('p')) #1
# print('apple'.find('k')) #-1

# print('abc'.isalpha())
# print('Ab'.isupper())
# print('ab'.islower())
# print('Title!'.istitle())

# print('wooooowoo'. replace('o','!', 2))
# print('a,b,c'.split(','))
# print('서울시 강남구 월곡동'.split()[0])

# print('!'.join('ssafy'))

# msg = 'hI! EVEryone, I\'m Ssafy'

# print(msg)
# print(msg.capitalize())
# print(msg.title())
# print(msg.lower())
# print(msg.swapcase())
# print(' '.join(['3','5','8','9']))

# cafe = ['a', 'b']
# print(cafe, id(cafe))
# cafe.insert(100000,'c')
# print(cafe, id(cafe))

# numbers = [1,2,3,1,1,1,2,2,2,3,3,2]
# re = numbers.sort()
# ree = sorted(numbers)

# print(re)
# print(ree)

# numbers = [1,2,3,1,1,1,2,2,2,3,3,2]
# numbers.sort()
# print(numbers)

# a = (1,2,3,5,1)
# print(a[0])

# day_name = ('월', '화', '수', '목', '금')
# print(day_name[-3])
# print(day_name *2)
# print(id(day_name))
# day_name += False, True
# print(day_name)
# print(id(day_name))

# my_dict = {'apple': '사과', 'banana':'바나나'}
# print(my_dict['apple'])
# b = my_dict.get('apple')
# print(b)
# my_dict.update(apple = '고구마')
# print(my_dict)
# for key in my_dict:
#     print(key)
# for i in my_dict.values():
#     print(i)
# for a, b in my_dict.items():
#     print(a, b)


# original_lst = [1,2,3]
# copy_lst = original_lst
# print(original_lst, copy_lst)
# copy_lst[0] = 'hello'
# print(original_lst, copy_lst)

# a = [1,2,3]
# b = a[:]
# b[0] = 5
# print(a,b)

# original_list = [1,2,3]
# copy_list = original_list
# print

#int
from re import A


# a=1
# b=a
# b=2
# print(a,b)

# a = 'a'
# b = a
# b = 'b'
# print(a,b)

# a = [1]
# b=a
# b[0] = 2
# print(a,b)

def func(arr):
    arr[0] = 'd'

if __name__ == '__main__':
    tmp = ['a', 'b', 'c']
    print(tmp)
    func(tmp)
    print(tmp)
    
