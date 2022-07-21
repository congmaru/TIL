#데일리실습 3-2
#문자열을 전달 받아 해당 문자열의 정중앙 문자를 출력하시오.
# 단, 문자열의 길이가 짝수일 경우에는 정중앙 문자 2개를 출력하라.
def func3():
    #1.문자열 입력
    sentence = input('문자열을 입력하세요 : ')
    #2.정중앙 글자 출력(홀수인 경우)
    if len(sentence) % 2 == 1:
        index = len(sentence) // 2
        print(sentence[index])   #정중앙 표시해줌
    #3.정중앙 글자 출력(짝수인 경우)
    else:
        index1 = len(sentence)//2 - 1
        index2 = len(sentence)//2
        print(sentence[index1])
        print(sentence[index2])

    # abcd
    # 0123
    # 길이 = 4 /2햇을 때 c나옴. 그 앞에 하나더까지 표기
    # abcdef
    # 012345
    # 길이 = 6/2햇을 때 3. d나옴. 그 앞에 하나더까지 표기

func3()


def func4():
    sen = input('문자열을 입력하세요 : ')
    if len(sen) %2 == 1:
        index = len(sen)//2
        print(sen[index])
    else:
        index1 = len(sen)//2 -1
        index2 = len(sen)//2
        print(sen[index1], sen[index2]) #가로로출력하려고
        
# abcdef
# 012345 길이 6 나눴을 때 3. 3이랑 그 앞에꺼 출력

func4()