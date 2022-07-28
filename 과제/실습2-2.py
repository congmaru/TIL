# 1.    문자열 s를 입력받아 아래와 같이 수정하고, 출력하라
# A.    모든 대문자는 소문자로 바꾸되, 가장 첫 번째 대문자는 바꾸지 않는다
# B.    문자열 앞뒤에 있는 특수 문자를 삭제한다.

def func1():
    Text = "string@@@"

    print(Text.upper())
    print(Text.capitalize())  #맨앞글자를 대문자로 바꾸기

    new_Text = ''.join(char for char in Text if char.isalnum()) #특수문자제거
    print(new_Text)

func1()


def func2():
    sen = "@~I NeVEr DrEamEd AbouT SuCCeSs, i woRkEd foR iT.!>!"
    new_sen = ''.join(char for char in sen if char.isalnum())
    print(new_sen)
    print(new_sen.capitalize())

func2()