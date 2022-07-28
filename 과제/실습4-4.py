word1 = input('첫 번째 이름을 입력하세요 : ')
word2  = input('두 번째 이름을 입력하세요 : ')

lst1 = list(word1)
lst2 = list(word2)

llst1 = []
llst2 = []
for w1 in lst1:
    llst1.append(ord(w1))
for w2 in lst2:
    llst2.append(ord(w2))

if sum(llst1) > sum(llst2):
    print(word1)
if sum(llst1) < sum(llst2):
    print(word2)
if sum(llst1) == sum(llst2):
    print(word1, word2)