class Doggy():

    num_of_dogs = 0 #클래스 변수. 
    birth_of_dogs = 0

    def __init__(self,name,type): #인스턴스변수. 생성자
        print('Doggy 클래스 생성자 호출')
        Doggy.birth()
        self.name = name
        self.type = type

    def __del__(self): #소멸자
        print('Doggy 소멸자 호출')
        Doggy.dead()


    @classmethod #클래스메서드. 클래스가 사용하는 함수
    def birth(cls):
        cls.num_of_dogs +=1
        cls.birth_of_dogs +=1

    @classmethod
    def dead(cls):
        cls.num_of_dogs -=1

    @classmethod
    def get_status(cls):
        print(f'현재남아있는 개의 수는 {cls.num_of_dogs}입니다')

    def bark(self):
        print(f'웡! 나는 {self.name}이다')
    
    
    
Doggy.get_status()
dog1 = Doggy('콩','시츄')
dog1.bark()
Doggy.get_status()
del dog1
Doggy.get_status()


#birth() 함수와 dead() 함수는 그냥 가독성을 위해 따로 뺀겁니다.
# init 과 del 안에서 직접 변수 수정해도 괜찮아요
# @classmethod 데코레이터는 클래스 변수를 쓸 때 사용합니다.
# 사실 없어도 정상 동작합니다 !!!
# 그렇지만, 클래스 변수 접근하는 메서드와 인스턴스 변수를 접근하는 메서드 를 구분하여 사용하는 것이 좋습니다.