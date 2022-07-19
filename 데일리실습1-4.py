#데일리실습1-4

result = 0

for i in range(1,10):
    if i % 2 == 0 or i % 7 == 0:
        result = result + 1
        
    print(sum(result))




s = set()

for i in range(1, 1000):
    if i % 2 == 0:
        s.add(i)

    if i % 7 == 0:
        s.add(i)

print(sum(s))


