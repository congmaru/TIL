#8-2

class Person():

    def __init__(self, name, age):
        self.name= name
        self.age= age

    @classmethod
    def detail(cls, name, year):
        age = 2022-int(year) +1 #age는 classmethod 내에서만 쓰는 지역변수
        return cls(name, age)

    def check_age(self):
        print(f'현재 나이는 {self.age}입니다')
        if self.age <19:
            return True
        else:
            return False
    
    
person = Person('김싸피', 28)
person.check_age()


person2 = Person.detail('테스트', 2000)
print('미성년자입니다') if person2.check_age() == True else print('성인입니다')

#내가 짜던 코드
#     def get_info(self):
#         print(f'이름:{self.name} / 나이 : {self.age}')

# class Detail(Person):
#     def __init__(self,name,age,birth_year):
#         super().__init__(name, age)
#         self.birth_year = birth_year

#     def check_age(self):
#         if self.age(self) > 19:
#             return False
#         else:
#             return True

# if __name__ == '__main__':
#     person1 = Detail('John', 10, 1994)
#     print(person1.check_age())