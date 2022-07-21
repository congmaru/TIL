boxes=['A', 'B', ['apple', 'banana', 'cherry']]
print(len(boxes))
print(boxes[2])
print(boxes[2][-1])
print(boxes[-1][1][0])



# 변수 boxes에 문자열 'A', 'B', 리스트 ['apple', 'banana', 'cherry']를 할당합니다.
boxes = ['A', 'B', ['apple', 'banana', 'cherry']]
# boxes의 길이를 len 함수를 이용하여 출력해 봅시다.
len(boxes)
# boxes의 3번째 요소를 인덱스로 접근하여 출력해 봅시다.
print(boxes[2])
# boxes의 3번째 요소들 중, 마지막 요소를 negative index로 접근하여 출력해 봅시다.
print(boxes[2][-1])
# boxes의 마지막 요소들 중, 두번째 요소의 첫번째 문자열을 출력해 봅시다.
print(boxes[2][1][0])


