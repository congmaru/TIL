### 8-1

김해피는 **구슬치기 대회**에 참가하였다. 모든 인원은 참가 번호를 부여받는데, 자신과 같은 참가 번호를 가진 사람과 구슬치기 게임을 진행하여야 한다. 단, 반드시 짝이 없는 한 명의 **깍두기**가 존재한다. 참가자들의 참가 번호 정보가 리스트로 주어질 때, **깍두기의 참가 번호를 출력하시오.**

A.    참가자 번호는 1번부터 시작합니다.

B.    깍두기는 한 명만 존재합니다.

C.    깍두기를 제외한 모든 참가자는 자신의 짝(자신과 같은 수)이 존재합니다.

```python
participants =  [3, 7, 100, 21, 13, 6, 5, 7, 5, 6, 3, 13, 21]
pair = []

for p in participants:
    pair.append(p)
    participants.remove(p)
    if pair[-1] in participants:
        participants.remove(p)
        pair.remove(p)

print(pair)
```

### 8-2

아래의 명세를 읽고 Python 클래스를 활용하여 사람(Person)을 표현하시오.

1.  사람은 이름과 나이를 가진다.

2.  사람을 인스턴스를 생성하는 방법은 2가지다.

A.    생성자

i.        이름과 나이를 인자로 받는다.

B.    details 클래스 메서드

i.        이름과 태어난 년도를 인자로 받는다.

3.  인스턴스의 나이를 확인하는 메서드 check_age를 만든다.

A.    미성년자의 기준을 미성년자 여부를 True, False로 반환한다. 미성년자는 19세를 기준으로 한다.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def details(cls, name, year):
        age = 2022-int(year)+1
        return cls(name, age)

    def check_age(self):
        print(f'현재 나이는 {self.age}입니다.')
        if self.age <= 19:
            print(f'{self.age}살로 미성년자입니다.')
            return True
        else:
            print(f'{self.age}살로 성인입니다')
            return False

person = Person('정혜수', 28)
person.check_age()

person2 = person.details('테스트', 2000)
person2.check_age()
```

### 8-3

아래의 명세를 읽고 Python 클래스를 활용하여 PublicTransport을 표현하시오.

A.     PublicTransport는 이름 name 과 요금 fare을 인스턴스 속성으로 가진다.

B.     탑승get_in, 하차get_off하는 메서드를 필요로 한다. 이 때, passenger의 수를 받는다.

C.     현재 탑승자 수를 알 수 있어야 한다.

D.     최종 수익을 계산하는 메소드 profit 은 요금과 전체 탑승자 수를 곱해서 계산한다.

```python
class PublicTransport:
    def __init__(self, name, fare): #A조건 달성
        self.name = name
        self.fare = fare
        self.total = 0

    def get_in(self, name):
        self.name += name
        self.total += name*self.fare

    def get_off(self, name):
        self.name =+ name

    def profit(self):
        print(f'현재 탑승중인 인원 : {self.name}/ 총 수익: {self.total}')

transport = PublicTransport(0, 100)
transport.get_in(20)
transport.get_off(10)

transport.profit()
___
현재 탑승중인 인원 : 10/ 총 수익: 2000
```

### 8-4

앞서 제작한 PublicTrransport의 subclass Bus클래스를 만들어라.

A. 탈수 있는 인원을 제한하기 위한 인스턴스 변수를 추가해라.

B. get_in 메서드를 오버라이딩하여 탈수있는 인원보다 많이 타려고 한다면 ‘더이상 탑승할수없습니다’문구를 출력하고 종료해라

### #8-2

```python
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2

    def get_area(self):
        return abs(self.p2.x-self.p1.x)*abs(self.p2.y-self.p1.y)

    def get_perimeter(self):
        return (abs(self.p2.x-self.p1.x)+abs(self.p2.y-self.p1.y))*2
    
    def is_square(self):
        return abs(self.p2.x-self.p1.x)==abs(self.p2.y-self.p1.y) #True를 따로 안써도 된다. 디폴트값

p1 = Point(1,3)
p2 = Point(3, 1)
r1 = Rectangle(p1, p2)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())

p3 = Point(3,7)
p4 = Point(6, 4)
r2 = Rectangle(p3, p4)
print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())
```

### #8-4

풀긴 풀었는데 오답체크부터는 또 해야한다.

다음주에 실습 1~8 full 정리 필수★