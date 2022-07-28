#작물과 가격이 함께 있는 리스트가 존재할 때, 가장 높은 가격을 가지고 있는 작물의 이름을 출력하라.
#단, 작물의 이름을 직접 입력하여 출력하지 않는다
crops = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]
# lst_1 = []
# for i in crops:
#     lst_1.append(i[0])
# lst_2 = []
# for i in crops:
#     lst_2.append(i[1])

# print(lst_1, lst_2)
# m_lst = max(lst_2)
# m_index = lst_2.index(m_lst)
# print(m_index)
# print(lst_1[m_index])
#야호 됐지롱~~~~

lst_name = []
lst_price = []
for i in crops:
    lst_name.append(i[0])
    lst_price.append(i[1])

max_price = max(lst_price)
idx_mprice = lst_price.index(max_price)
print(lst_name[idx_mprice])