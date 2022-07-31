### 7-1

아래와 같이 국적을 출력할 수 있는 클래스 Nationality를 작성하시오.

korea_nationality = Nationality("대한민국")

**print**(korea_nationality) *# 나의 국적은 대한민국*

```python
class Nationality:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return (f'나의 국적은 {self.name}')

korea_nationality = Nationality("대한민국")
print(korea_nationality) # 나의 국적은 대한민국
```

→ 생성자 메서드 init에 print(f'나의 국적은 {self.name}')를 적었는데, 그건 X! return 값을 써서 함수를 완성해야 하며 TypeError: **init**() should return None, not 'str'가 뜨므로 str로 따로 빼야한다.

### 7-2 ★

Q. 끝말잇기 단어의 리스트가 주어졌을 때, 몇 번째 사람이 탈락하는지 확인하는 함수 wordrelay를 작성하시오.

조건 : A. 앞서 입력된 단어의 마지막 문자로 시작하는 단어를 말해야 합니다.B. 끝말잇기를 틀리거나 이전에 등장했던 단어를 사용하는 경우, 지게 됩니다.C. done을 입력할 때까지 끝말잇기를 시행합니다.

ver. 교수님이 주신 스켈레톤 코드를 토대로 완성

```python
class Wordrelay():
    # 1. words 리스트를 전달받아 인스턴스 변수로 만드는 생성자를 구현하세요
    def __init__(self, words):
        self.words = words

    # 2. 실패와 성공 여부를 결정하는 함수를 구현하세요
    #끝말잇기를 틀리거나, 이전에 등장했던 단어를 사용하는 경우 실패
    def check_fail(self):
        past_words = [self.words[0]]
        if len(self.words) == 1: #탈락. 숫자 1로 지정해 첫번째에서 탈락햇다는 문구가 나와야함
            return 1
        for i in range(1, len(self.words)): #첫번째는 무조건 통과이므로 2번째부터 끝까지.
            if self.words[i] == 'done': #done이 입력된 경우 끝말잇기 끝. 이걸 -1로 지정
                return -1 
            if self.words[i][0] != past_words[-1][-1]: #마지막으로 들어간 단어가 맨 끝에있으니까 [-1]을 쓰는게 맞다.
                return i+1
            elif self.words[i] in past_words: #중복되는 단어가 있을시 실패
                return i+1

            past_words.append(self.words[i]) #past_word에 꼐속 self.words가 추가되어야한다. 리스트는 순서가 있으므로 인덱스 가능! past_words에 대한 정의를 for문안에서 해야하기 때문에 위치가 밑으로 내려올 수 밖에 없음

        return -1 #전부 다 통과했을 때 끝말잇기 끝
    
    # 3. 결과를 돌려주는 함수를 작성하세요.
    #위의 내용을 토대로 끝말잇기가 승패관련없이 끝나면 -1. 그 외에는 몇번째 사람이 탈락했는지 문구 출력.
    def get_result(self):
        result = self.check_fail() #result자체가 check_fail함수의 결과값이다.
        if result == -1:
            return '탈락한 사람이 없다'
        else:
            return f'{result}번째 사람이 탈락했다'

if __name__ == '__main__':
    words = ["round","dream","magnet","tweet","tweet","trick","kiwi"]
    wordrelay = Wordrelay(words)
    print(wordrelay.get_result()) # 5번째 참가자가 탈락하였습니다.
```

### 7-3

add, substract, multuply, divide 메소드를 가진 Calculator 클래스를 생성하고, 아래의 계산 결과를 출력하라. 단, 숫자는 0으로 나눌 수 없다. 이 경우, 예외처리로 0으로 나눌 수 없습니다.를 출력하라

ex) 1 + 2, 2 – 1, 3 * 4, 4 / 0

```python
class Calculator:
    # def __init__(self,a,b):
    #     self.a = a
    #     self.b = b
    
    def add(self,a,b):
        return a+b

    def minus(self,a,b):
        return a-b
    
    def multiple(self,a,b):
        return a*b

    def divide(self,a,b):
        try:
            return a/b
        except:
            return '0으로 나눌 수 없다'

result = Calculator()
print(result.add(2, 3)) #5
print(result.minus(2, 1)) #1
print(result.multiple(3, 4)) #12
print(result.divide(4, 0)) #0으로 나눌 수 없다.
```

→클래스 정의 아래 생성자 메서드는 이 문제에서 없어야 한다. 왜냐하면 인스턴스 변수가 필요하지 않기 때문. result는 함수를 쓰기 위한 변수로 지정한 것이고, 그 아래의 result.add(2,3) 등은 함수에 내장된 함수를 사용하는 것

### 7-4

카 쉐어링 서비스 요금 계산

A. 대여는 10분 단위로 가능

B. 대여 요금 : 10분당 1,200원

C. 보험료 : 30분당 525원(50분 빌리면 1시간으로 계산)

D. 주행요금: km당 170원(100km가 넘어가면 넘어간 부분에 대하여 할인이 50%적용)

참고함수  math.ceil

예시 : fee(600,50) = 91000, fee(600, 110) = 100350(600분에 110km를 의미함)

### cf.  math.ceil() : 주어진 숫자보다 크거나 같은 숫자중 가장 작은 숫자를 int로 반환 ex. math.ceil(.95) = 1, math.ceil(7.004) =8

```python
import math #math.ceil 함수를 쓰기위해 불러옴

class Fee(): #클래스 정의
    def __init__(self, time, distance): #인스턴스변수 정의. 생성자메서드
        self.time = time
        self.distance = distance #time과 distance는 인스턴스변수

    # 렌탈 비용 계산
    def get_total_rental(self): #인스턴스메서드
        return self.time/10 *1200

    # 보험료 계산
    def get_total_insurance(self):
        return math.ceil(self.time/30) *525

    # 주행 요금 계산
    def get_total_drive(self):
        if self.distance >= 100 :
            return 100*170 + (self.distance-100)*85
        else:
            return self.distance*170

    def get_fee(self):
        self.get_total_rental() #각각 함수를 self에 적용시켜야함
        self.get_total_insurance()
        self.get_total_drive()

        return self.get_total_rental() + self.get_total_insurance() + self.get_total_drive()

#답출력방식 ver1.
if __name__ == '__main__':
    time, distance = map(int, input('렌탈비용과 주행거리를 띄워쓰기로 구분하여 입력하세요 : ').split())
    fee_instance = Fee(time, distance)
    print(fee_instance.get_fee())

#답출력방식 ver2. 
fee = Fee(600, 90) #인스턴스
print(fee.get_fee()) #인스턴스.인스턴스메서드 적용
```

### 7-5

페어프로그래밍 프로그램 만들기

1. 초기화 메서드는 인자로 학생이름으로 구성된 리스트를 받아 인스턴스 변수에 할당
2. pick(n)메서드는 학생들 명단에서 인자 n명만큼 랜덤으로 추출하여 return
3. match_pair()메서드는 학생들 명단을 랜덤으로 2명씩 매칭해준다. 이때 만약 명단수가 홀수이면 한팀만 3명으로 구성한다.

### cf. random.sample(seq or set, N): 첫번째 매개변수는 시퀀스타입(튜플, 문자열, range, 리스트)나 set타입을 받고, 두번째 매개변수로 랜덤하게 뽑을 인자의 개수를 넣는다. 즉, 첫번재로 받은 인자중 N개의 랜덤한 인자를 뽑아 리스트로 만들어 반환해준다.

```python
import random

class Students():
    # 1. 초기화 메서드 작성
    def __init__(self, students):
        self.students = students

    # 2. 학생들 인자에서 인자 n 명 만큼 랜덤으로 추출하여 return 하는 pick 함수 작성
    # 참고 - random.sample 함수를 검색해보세요.
    def pick(self,n):
        return random.sample(self.students, n) #인스턴수 변수에서 n개만큼 랜덤하게 뽑는 함수

    # 3. 랜덤으로 2명(명단의 수가 홀수면 한 팀은 3명) 매칭하여 리스트로 반환하는 함수 match_pair 작성
    def match_pair(self):
        pair_list = []
        while len(self.students)>0: 
            if len(self.students) <=3:
                pair_list.append(self.students)
                break
            else:
                picked = self.pick(2)
                pair_list.append(picked)
                self.students.remove(picked[0])
                self.students.remove(picked[1])
        return pair_list

if __name__ == '__main__':
    students_list = ['김싸피', '금해피', '테스트', '철수킴', '박영희']
    students = Students(students_list)
    print(students.match_pair())
```

### #7-2

개의 속성과 행위를 정의하는 Doggy 클래스를 만들어라

a.초기화메서드는 인자로 개의 이름과 견종을 받아 인스턴수 변수에 할당

b.bark()메서드를 호출하면 개가 짖을 수 있다.

c. 클래스 변수는 태어난 개의 숫자와 현재있는 개의 숫자를 기록하는 변수로 구성. 개가 태어나면 num_of_dogs 와 birth_of_dogs의 값이 1씩 증가. 개가 죽으면 num_of_dogs 값이 1감소

d. get_status()메서드를 호출하면 birth_of_dogs와 num_of_dogs의 수를 출력할 수 있다. 

```python

class Doggy: #클래스 정의
    num_of_dogs = 0 #클래스변수
    birth_of_dogs = 0
    
    def __init__(self, name, type): #생성자 메서드. 인스턴수 변수 name, type 정의
        self.name = name
        self.type = type
        print('Doggy 클래스 생성자 호출')
        Doggy.birth()

    def __del__(self): #소멸자 메서드
        print('Doggy 클래스 소멸자 호출')
        Doggy.dead()

    @classmethod #클래스메서드. cls변수에 작용하며 전체 공용
    def birth(cls):
        cls.num_of_dogs +=1
        cls.birth_of_dogs +=1

    @classmethod
    def dead(cls):
        cls.num_of_dogs -=1

    @classmethod
    def get_status(cls):
        print(f'현재 남아있는 개는 {cls.num_of_dogs}마리이고 태어난 개는 {cls.birth_of_dogs}이다')

    def bark(self): #인스턴스메서드. self변수에 작용하며 각각용
        print(f'웡! 나는 {self.name}이다!')

Doggy.get_status() 
dog1 = Doggy('비호','치와와')
dog1.bark()
Doggy.get_status()
del dog1
Doggy.get_status()
______
현재 남아있는 개는 0마리이고 태어난 개는 0이다 #클래스메서드 실행됨
Doggy 클래스 생성자 호출 #인스턴스-생성자메서드 실행됨
웡! 나는 비호이다! #bark 인스턴스메서드 실행
현재 남아있는 개는 1마리이고 태어난 개는 1이다 #클래스메서드 실행
Doggy 클래스 소멸자 호출 #소멸자메서드 실행
현재 남아있는 개는 0마리이고 태어난 개는 1이다 #클래스메서드 실행
```

### #7-4

주어진 수가 1이 될때까지 다음 작업을 반복하면 모든 수를 1로 만들수있다는 추측이다.

1. 입력된 수가 짝수라면 2로 나눔
2. 입력된 수가 홀수라면 3을 곱하고 1을 더함
3. 결과로 나온 수에 같은 작업을 1이 될때까지 반복한다.

위 작업을 몇번이나 반복해야하는지 반환하는 함수 collatz()를 작성하시오. 단, 작업을 500번 반복해도 1이 되지않는다면 -1을 반환하시오.

```python
def collatz(n):
    e = 500         # 500번 이상 순회하면 안되기 때문에 500을 미리 변수로 만들어줌
    s = -1          # 몇번의 과정인가? 를 위한 변수, 순회를 9번 해도 과정은 8번이기 때문에 미리 -1로 세팅
    while e > 0:
        e -= 1          
        s += 1 
        if n != 1:     # n이란 변수로 계산을 할 것이기 때문에 n이 1이 아닌 상황에만 돌려준다.
            if n % 2 == 0: 
                n /= 2
            else:
                n = (n * 3) + 1                
        else: # n이 1이 된 조건
            return s
    return '-1' # 500번 이상 돌려도 1이 나오지 않는 경우 출력될 문자
num = int(input())
print(collatz(num))
```

→와우. 유명한 문제인가 보다. 단순히 함수를 만들라고 했으므로 따로 class 등을 만들 필요없다.
