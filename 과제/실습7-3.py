#7-3

class Calculator:
    #생성자 필요없음. 인스턴스변수가 필요하지 않기때문에
    def __init__(self):
            print(self)
    
    def add(self,a,b):
        return a+b
    def substrack(self,a,b):
        return a-b
    def multiply(self, a,b):
        return a*b
    def divide(self,a,b):
        try:
            return a/b
        except:
            return '0으로는 나눌 수 없습니다'
    
cal = Calculator()

print(cal.add(2,3))
print(cal.substrack(2,3))
print(cal.multiply(2,3))
print(cal.divide(2,3))
print(cal.divide(2,0))