class Calculator():
    def add(self, a, b): #인스턴스메서드
        return a + b

    def substract(self, a, b):
        return a - b

    def multiple(self, a, b):
        return a * b

    def divide(self, a, b):
        try:
            return a / b
        except:
            return '0으로 나눌 수 없습니다'

result = Calculator()

print(result.add(2, 3))
print(result.substract(2, 1))
print(result.multiple(3, 4))
print(result.divide(4, 0))