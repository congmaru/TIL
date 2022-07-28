# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def check_password_length(password):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    a = len(password)  #비밀번호의 길이를 a로 지정후
    if 8 <= a <= 32:  #if문을 사용하여 범위지정하여 결과값을 낸다.
        return True
    else:
        return False


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    password = 'q1w2e3r4'
    print(check_password_length(password)) # True
