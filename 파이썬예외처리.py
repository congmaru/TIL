a = [1,2,3]

for i in range(4):
    try:
        print(a[i])
    except:
        print('잘못된 인덱스 접근입니다.')
    else:
        print('에러없음')
    finally:
        print('에러와 상관없이 수행')


# try: 
#     실행할 코드
# except:
# 에러발생시 수행할 코드
# else:
# 에러 없을 시 수행할 코드
# finally:
# 에러와 상관없이 수행할 코드