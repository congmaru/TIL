#5-4. 데일리실습 4-3과 비슷
#같은 숫자가 한개나 두개 들어있는 리스트가 주어짐
#숫자가 한개만 있는 요소들의 합을 수하는 함수를 작성해라

def sum_of_repeat_number(n_lst):
    s_lst = []
    for n in n_lst:
        if n_lst.count(n) == 1:
            s_lst.append(n)
        else:
            pass

    print(s_lst)
    result = sum(s_lst)
    return result

n_lst = [4,4,5,8,10,4]

print(sum_of_repeat_number(n_lst))
