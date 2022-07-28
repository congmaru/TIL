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


class Dog(Animal):
    def __init__(self):
        print('Dog class 생성자')


    def bark(self):
        print('짖는다')


    def wag(self):
        print('꼬리를 흔든다')