class Doggy():

    num_of_dogs = 0
    birth_of_dogs = 0

    def __init__(self,name,type):
        print('Doggy 클래스 생성자 호출')
        Doggy.birth()
        self.name = name
        self.type = type

    def __del__(self):
        print('Doggy 소멸자 호출')
        Doggy.dead()


    @classmethod
    def birth(cls):
        cls.num_of_dogs +=1
        cls.birth_of_dogs +=1

    @classmethod
    def dead(cls):
        cls.num_of_dogs -=1

    @classmethod
    def get_result(cls):
        print(f'현재남아있는 개의 수는 {cls.num_of_dogs}입니다')

    def bark(self):
        print(f'월월! 나는 {self.name}이다')
    
Doggy.get_status()
dog1 = Doggy('콩','시츄')
dog1.bark()
Doggy.get_status()
del dog1
Doggy.get_status()