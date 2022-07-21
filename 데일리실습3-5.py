#데일리실습 3-5
#여러 개의 소금물을 섞었을 때, 혼합된 소금물의 퍼센트 농도와 양을 계산하는 프로그램을 만드시오
#조건 소금물의 퍼센트 농도와 소금물의 양을 입력하고, Done을 입력하면 혼합물의 퍼센트 농도와 양이 출력되도록 하시오
#최대 5개의 소금물을 입력할 수 있다
#출력된 혼합물의 퍼센트 농도와 양이 소수점 2자리를 넘어갈 경우, 반올림하여 2번째 자리까지만 나타내시오.

def func9():
    density_list = []
    water_list = []

    while True:
        menu = input(f'{len(density_list)+1} : 소금물의 퍼센트농도와 양을 띄어쓰기로 구분하여 입력하세요(Done 입력시 최종 계산):')
        if menu == 'Done':
            break

        density_list.append(float(menu.split()[0])) #퍼센트농도
        water_list.append(float(menu.split()[1])) #소금물의 양

 
        if len(density_list) == 5:
            break
    # print('density_list =', density_list)
    # print('water_list = ', water_list)

    solt_list = []
    for index in range((len(density_list))):
        solt = density_list[index] * water_list[index] / 100
        solt_list.append((solt))

    result_density = (sum(solt_list) / sum(water_list)) * 100

    print(f'혼합물 퍼센트 농도 : {round(result_density,2)}% / 혼합물의 양 : {sum(water_list)}')
    

func9()


def calculate(dic):
    sumwater=0
    sumsalt=0
    for x in dic:
        sumwater+=x
        sumsalt+=x(dic[x]/100)
    density=sumsalt/sumwater100
    print(round(density,2))

n=5
water={}
while n>0:
    s=input()
    if(s=='Done'):
        break
    else :
        x,y=map(int,s.split())
        water[x]=y
    n-=1
calculate(water)

