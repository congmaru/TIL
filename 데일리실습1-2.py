total = int(input('게시글의 총 갯수를 입력하세요 : '))
page = int(input('한 페이지에 필요한 게시글 수 : '))
result = int(total/page)

if int(total/page) < result:
    result += 1
else :
    Print(result)

print('정답 : ', result)
        