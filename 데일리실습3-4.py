#여러 사람의 혈액형(A, B, AB, O)에 대한 정보가 담긴 list를 전달 받아, key는 혈액형의 종류, value는 사람 수인 dictionary를 만드시오.

def func6():
    blood_types = [ 'A','A','O', 'B', 'A', 'O', 'AB','O', 'A', 'B', 'O', 'B', 'AB']
    count_dict = {
        'A':0,
        'B':0,
        'AB':0,
        'O' :0
    }
    for blood in blood_types:
        count_dict[blood] += 1
    print(count_dict)

func6()
