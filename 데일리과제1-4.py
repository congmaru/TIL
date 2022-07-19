##데일리과제1-4

s = input('숫자를 입력해주세요 : ')
number=list(s)
number=list(map(int,number))
sum_number=sum(number)
print(sum_number)





##강사님풀이
s_list = list(s)

result = 0
for i in s_list:
    result = result + int(i)

print(result)

