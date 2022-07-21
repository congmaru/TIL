def f(x):
    return x+5

numList = [1,2,3,4,5]

#print(list(map(f, numList)))

tempList=[]
for i in numList:
    tempList.append(f(i))

print(tempList)

