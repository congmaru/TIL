# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def average(scores):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    sum_s = sum(scores) #스코어의 전체 합계
    len_s = len(scores) #스코어의 전체 길이(갯수)
    average = sum_s/len_s #평균 = 총합/갯수
    return average


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    scores = [80, 90, 85, 75]
    print(average(scores)) # 82.5
