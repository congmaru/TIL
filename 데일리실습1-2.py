#데일리실습 1-2

total = int(input('게시글의 총 갯수를 입력하세요 : '))
page = int(input('한 페이지에 필요한 게시글 수 : '))
result = int(total//page)

if float(total/page) > result:  #int는 버림되기 때문에 실수형인 float을 써야함
    result = result + 1
    print('정답 : ', result)
else :
    print('정답 : ', result)
    
    

        