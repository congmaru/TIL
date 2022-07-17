A, B = input().split()
A = int(A)
B = int(B)
result = ""

if A == 1:
    if B == 2:
        print('B')
    elif B == 3:
        print('A')

if A == 2 :
    if B == 1:
        print('A')
    elif B == 3:
        print('B')

if A == 3:
    if B == 1:
        print('B')
    elif B == 2:
        print('A')

print(result)





