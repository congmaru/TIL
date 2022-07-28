# 현실 세계의 구조를 추상화 한 것
# 사람, 개는 동물 ( 동물이 가지는 공통적인 특징을 가짐 )
# 각각 다른 부분도 존재 ( 상속 받아서 구현 )
class Animal():
    def __init__(self):
        print('Animal class 생성자')


    def walk(self):
        print('걷는다')

    
    def eat(self):
        print('먹는다')


class Human(Animal):
    def __init__(self):
        print('Human class 생성자')


    def talk(self):
        print('말을 한다')


    def ssafy(self):
        print('싸피 수업을 듣는다')

    # 메서드 오버라이딩
    # overrde
    # 이런식으로 주석으로 표시해주는 것이 좋다
    def walk(self):
        print('두 발로 걷는다 !')


class Dog(Animal):
    def __init__(self):
        print('Dog class 생성자')

    # 메서드 오버라이딩
    # overrde
    # 이런식으로 주석으로 표시해주는 것이 좋다
    def walk(self):
        print('네 발로 걷는다 !')


    def bark(self):
        print('짖는다')


    def wag(self):
        print('꼬리를 흔든다')

#__________________________
from test_module import Animal, Human, Dog

# 공통적으로 가지고 있는 부분
animal = Animal()
animal.walk()
animal.eat()
# ---------------------------------
# Human 클래스
human = Human()
# Human 클래스만 가진 함수
human.talk()
human.ssafy()

# 상속받아서 실행하는 함수
human.eat()

# 메서드 오버라이딩을 통해 Human 의 함수로 덮어씀
human.walk()

# ---------------------------------
# Dog 클래스 가진 부분
dog = Dog()
# Dog 클래스만 가진 부분
dog.bark()
dog.wag()

# 상속받아서 실행하는 함수
dog.eat()

# 메서드 오버라이딩을 통해 dog 의 함수로 덮어씀
dog.walk()