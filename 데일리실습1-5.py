#데일리실습1-5
def func2():
    wide = int(input())
    height = int(input())
    
    for _ in range(height):
        for _ in range(wide):
            print('*', end ='')
        print()

func2()
    


def func3():

    wide = int(input())
    height = int(input())

    for _ in range(height):
        print('*' * wide)

func3()



def func4():

    wide = int(input())
    height = int(input())

    tup = (wide, height)

    for _ in range(tup[1]):
        
        print('*' * tup[0])

func4()