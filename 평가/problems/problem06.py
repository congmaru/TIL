# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def caesar(word, n):
    # 여기에 코드를 작성하여 함수를 완성합니다.
    # 대소문자 구별하여 암호화. 
    # A 를 기준으로 생각한다. A와의 차이에 n을 더한 것을 알파벳 갯수만큼 나눔 : 핵심은 시작점으로 다시 돌아가는 방법
    li = list(word)
    for i in range(len(li)):
        if li[i].isupper():
            li[i] = chr(65 + ((ord(li[i])-65 +n)%26))
        elif li[i].islower():
            li[i] = chr(97+ ((ord(li[i])-97 +n)%26))
    return ''.join(li)

# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    print(caesar('apple', 5))
    # fuuqj
    print(caesar('ssafy', 1))
    # ttbgz
    print(caesar('Python', 10))
    # Zidryx