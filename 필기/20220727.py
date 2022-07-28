# from calendar import c


# class Person:
#     def __init__(self,name): #인스턴스변수 정의 #셀프는 자기자신을 의미하고
#         self.name = name  #첫번째 parameter는 무조건 self를 사용해야함

# john = Person('john') #인스턴스변수 접근
# print(john.name)
# john.name = 'John Kim' #인스턴수변수 할당
# print(john.name)

# class Circle():
#     pi = 3.14 #클래스변수. 공용.

#     def __init__(self,r):
#         self.r = r   #pi변수 정의x. 그러면 자동으로 위의 클래스변수로 올라감

# c1 = Circle(5)
# c2 = Circle(10)

# print(Circle.pi)
# print(c1.pi)
# print(c2.pi)
# Circle.pi = 5
# print(Circle.pi)
# print(c1.pi)
# print(c2.pi)

# class Person:
#     count = 0 #공용

#     def __init__(self, name): #생성자
#         self.name = name
#         Person.count += 1

# person1 = Person('아이유') 
# person2 = Person('이찬혁')

# print(Person.count)

