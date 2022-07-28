
class Nationality():
    def __init__(self,nation):
        self.nation = nation
    
    def __str__(self):
        return f'나의국적은 {self.nation}'


korea_nationality = Nationality('대한민국')
print(korea_nationality) #나의국적은 대한민국

#7-1
class Nationality:
    def __init__(self, nation): #인스턴스변수
        self.nation = nation
    
    def __str__(self): #인스턴스변수
        return f'나의 국적은 {self.nation}'

korea_nationality = Nationality("대한민국")
print(korea_nationality) # 나의 국적은 대한민국
