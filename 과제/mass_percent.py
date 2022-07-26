def mass_percent():
    density_lst = []
    water_lst = []
    while True:
        menu = input(f'{len(density_lst)+1} : 소금물의 퍼센트농도와 양을 띄어쓰기로 구분하여 입력. (Done입력시 최종계산)')
        if menu == 'Done':
            break
        
        density_lst.append(float(menu.split()[0])) #퍼센트농도
        water_lst.append(float(menu.split()[1])) #소금물의 양

    salt_lst = []
    for index in range(len(density_lst)):
        salt = density_lst[index]*water_lst[index]/100
        salt_lst.append(salt)
    result_density = (sum(salt_lst)/sum(water_lst)) * 100
    result = {f'혼합물퍼센트농도: {round(result_density,2)}%/ 혼합물의 양 {sum(water_lst)}'}
    return result

print(mass_percent())