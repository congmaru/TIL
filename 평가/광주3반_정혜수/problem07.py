# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def dec_to_bin(n):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    #먼저 숫자를 입력받는다. int(input())활용
    #range함수와 %, // 등의 연산자. 그리고 for문. if문을 이용하면 풀릴 것 같다.
    # n = int(input('숫자를 입력하세요'))
    # a = n // 2 #2로나눈 몫
    # b = n % 2 #2로나눈 나머지
    # lst = []
    # if a >= b:
    #     lst.append(b)
    # return n

# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    print(dec_to_bin(10))
    # 1010
    print(dec_to_bin(5))
    # 101
    print(dec_to_bin(50))
    # 110010