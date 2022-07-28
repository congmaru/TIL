# from 실습8-3 import PublicTransport (함수구현하기 )주소 제대로 적기

class Bus(PublicTransport):
    def __init__(self, limit, passengers, fee):
        self.limit = limit
        #버스에서도 탑승객 인스턴스 변수 쓰고싶다.
        super().__init__(passengers, fee)


#   def test(self):
#         print(self.limit) #100
#         print(self.passengers) #0
#         print(self.fee) #1200
#         print(self.total) #0   


#ovveride
def get_in(self, passenger):
    if self.passengers + passenger >self.limit:
        #제한인원에 딱 맞도록 태움
        #90명탑승중/15명타려고함/10명태우고 5명못탐
        #제한인원-현재탑승인원 = 탈수있는인원
        new_passengers = self.limit - self.passengers   
        super().get_in(self.limit - self.passengers)
        print('더이상 탑승할 수 없습니다')
        print(f'못탄인원은 {passenger - (new_passengers)}명입니다')
    else:
        self.passengers +=passenger
        self.total += passenger*self.fee
        print(f'현재탑승중인 인원 : {self.passengers}')

if name__ == '__main__':
    bus = Bus(100, 0, 1200)
    bus.test()
    bus.get_in(20) #사용가능? yes. 부모가 get in 함수를 가지고 있기 때문. #여기서 사용한 getin은 부모꺼? no 자식꺼. (이부분 다시 체크하기)

    