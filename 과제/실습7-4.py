#실습7-4
import math

class Css:
    def __init__(self,time,km):
        self.time = time
        self.km = km
        

    #대여료
    def rental_fee(self):
        return 1200 *self.time/10

    #보험료
    def insu_fee(self):
        return 525*math.ceil(self.time/30)

    #주행요금
    def dri_fee(self):
        if self.km>100:
            return 170*100 + 85*(self.km-100)
        else:
            return 170*self.km

    # def fee(Css):
    #     fee.rental_fee()
    #     fee.insu_fee()
    #     fee.dri_fee()

    #     return fee.rental_fee()+fee.insu_fee()+fee.dri_fee()


fee = Css(600,110)
a =fee.rental_fee()
b = fee.insu_fee()
c =fee.dri_fee()
total = a+b+c
print(total)


#fee(600,50) = 91000
#fee(600,110) = 100350