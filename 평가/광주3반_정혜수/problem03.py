# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def get_user_id(data):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    return str(data['id']) #data 딕셔너리의 id 키의 밸류를 받아왔고, type해보니 str이 뜬다.
    
    # id의 밸류값이 숫자일 때 실험해보면
    # idd = {'idd': 12425}
    # a = idd['idd']
    # print(type(a)) #여기서 class int가 나오므로 str로 변환해줘야 한다.


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    user_data = {
        "id": "jungssafy",
        "password": "q1w2e3r4",
        "password_confirm": "q1w2e3r4"
    }
    print(get_user_id(user_data)) # 'jungssafy'
