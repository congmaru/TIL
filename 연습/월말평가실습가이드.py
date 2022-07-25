# my_dict = {'apple': '사과', 'banana':'바나나'}


# my_dict.update(grape = "썩사") #딕셔너리에 값 추가되는 것
# print(my_dict)
# my_dict['grape'] = '썩사' #딕셔너리에 값 추가되는 것. 
# print(my_dict)

# my_lst = [1,2,3]
# my_lst2 = my_lst
# print(my_lst2, my_lst) #[1, 2, 3] [1, 2, 3]

# my_lst[0] = 0
# print(my_lst2, my_lst) #[1, 2, 3] [1, 2, 3] 
#결국 my_lst와 my_lst2는 동일하며, 그냥 부르는 변수를 하나 더 추가하는 것과 같다.
#얕은 복사를 통해 복사한 리스트들 모두가 영향을 받게 된다.

#깊은 복사를 사용하게 되면 복사 대상 리스트를 새로 만들어서 거기에 이름을 연결시킨다.
import copy

my_lst = [1,2,3]
my_lst2 = my_lst
my_lst3 = copy.deepcopy(my_lst)
my_lst[0] = -1
print(my_lst, my_lst2, my_lst3)
