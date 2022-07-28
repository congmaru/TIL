#과제 8-2
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    #Rextangle 클래스메서드
    #넓이반환
    def get_area(self):
        return abs(self.p2.x-self.p1.x)*abs(self.p2.y-self.p1.y)

    #둘레길이 반환
    def get_perimeter(self):
        return (abs(self.p2.x-self.p1.x)+abs(self.p2.y-self.p1.y))*2
    
    #정사각형여부
    def is_square(self):
        return abs(self.p2.x-self.p1.x)==abs(self.p2.y-self.p1.y) #True를 따로 안써도 되는거구나

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