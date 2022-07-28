# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def caesar(word, n):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    # 우선 단어를 입력받은 뒤 각 자리로 쪼갠다. input, split 활용
    #각 대문자와 소문자에 해당하는 숫자와 알파벳을 리스트화한 자료가 필요
    # 각 자리의 알파벳에 해당하는 자릿수를 인덱스한다.
    # 그리고 해당하는 n만큼의 숫자를 더한뒤 그 숫자에 해당하는 알파벳을 불러오면 된다.

    words = input('단어를 한글자씩 입력하시오').split(' ')
    lst = []
    for i in words:
        o_words = ord(i)
        lst.append(o_words)
    
        
        



# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    print(caesar('apple', 5))
    # fuuqj
    print(caesar('ssafy', 1))
    # ttbgz
    print(caesar('Python', 10))
    # Zidryx