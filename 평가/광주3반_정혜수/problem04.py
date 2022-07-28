# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
from operator import truediv


def check_duplicate_id(target_username, username_list):
    pass
    #여기에 코드를 작성하여 함수를 완성합니다.
    #1번코드. username_lst의 각 요소와 target_username을 비교해 리턴값을 얻는 방식으로 코드를 짰다.
    #하지만 각자 돌려야한다는 번거로움이 존재함.
    # if target_username == username_list[0]:
    #     return True
    # elif target_username == username_list[1]:
    #     return True
    # else:
    #     return False

    #때문에 2번코드로 바꿨다. if~ in을 썼으며 훨씬 간단한 코드가 나온다.
    if target_username in username_list:
        return True
    else:
        return False

     

    

# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    target_username = 'jungssafy'
    username_list = ['kimssafy', 'jungssafy']
    print(check_duplicate_id(target_username, username_list)) # True
