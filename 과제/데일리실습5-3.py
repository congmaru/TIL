#특수문자 없애고, 소문자로 만들되 가장 첫번째 대문자는 바꾸지 않는다.
#첫번째 방식

s = '@#~I NeVEr DrEamEd AbouT SuCCeSs, i woRkEd foR iT.!>!'
def sent(s):
    s1 = s.strip('~!@#$%>')
    s2 = s1.lower()
    s3 = s2.capitalize()
    return s3


print(sent(s))
