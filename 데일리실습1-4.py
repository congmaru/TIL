#데일리실습1-4

result = 0
for i in range(1,1000):
    if i // 2 == 0 or i // 7 == 0:
        result += i
        
    print(result)


    #근데 이거 결과값이 계속 나온다. 어떻게 끝내지?
    