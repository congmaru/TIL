#여러 사람의 혈액형(A, B, AB, O)에 대한 정보가 담긴 list를 전달 받아
#key는 혈액형의 종류, value는 사람 수인 dictionary를 만드시오.
#딕셔너리의 좋은 활용!

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

 # #카운트방법1
    # count_A = 0
    # count_B = 0
    # count_O = 0
    # count_AB = 0
    # #카운트방법2
    # count_list = [0,0,0,0]
    #카운트방법3
    # count_dict = {
    #     'A':0,
    #     'B':0,
    #     'AB':0,
    #     'O' :0}

def func7():
    blood_types = [ 'A','A','O', 'B', 'A', 'O', 'AB','O', 'A', 'B', 'O', 'B', 'AB']
    blood=set(blood_types)
    blood_dict={}
    for x in blood:
        blood_dict[x]=blood_types.count(x)

    print(blood_dict)

func7()


def func8():
    blood_types = [ 'A','A','O', 'B', 'A', 'O', 'AB','O', 'A', 'B', 'O', 'B', 'AB']
    count_dict = {}
    for blood in blood_types:
        try:
            count_dict[blood] += 1
        except:
            count_dict[blood] = 1 

func8()