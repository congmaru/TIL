#데일리실습 3-3
#Dictionary로 이루어진 list를 전달 받아 모든 dictionary의 'age' key에 해당하는 value들의 합을 구하시오.
#1. List 안의 Dictionary요소 하나하나에 접근하는 방법
#2. Dictionary에서 key값으로 value를 꺼내오는 방법
def func5():
    infos = [{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}]
    result = 0
    for info in infos: 
        #print(info.get('age'))  둘다 같음
        print(info['age'])
        result += info['age']
    print(result)
func5()

def func6():
    infos = [{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}]
    result = 0
    for info in infos:
        print(info.get('age'))
        result += info.get('age')
    print(result)

func6() #복습