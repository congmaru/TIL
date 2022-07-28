#8-3, 8-4
# 탑승객 수(passengers) 와 요금(fare)를 받는다.
class PublicTransport():
    # 탑승객 수와 요금을 입력받아 초기화하는 메서드
    def __init__(self, passengers, fee):
        self.passengers = passengers
        #인당요금
        self.fee = fee
        #탑승할때마다 요금 추가
        self.total = 0

    # 탑승 메서드
    # passenger 를 파라미터로 받음
    # 새로 탄 승객에 따라 총 요금에 추가. 
    def get_in(self, passenger):
        self.passengers += passenger
        self.total += passenger * self.fee #self.fee는 인스턴스변수/ passenger는 로컬변수로 self가 없음

    # 내리는 메서드
    # 승객 수만 감소
    def get_off(self, passenger):
        self.passengers -= passenger
    

    # 현재 탑승중인 인원과 최종 수익을 출력
    def profit(self):
        print(f'현재 탑승중인 인원 : {self.passengers} /총수익 : {self.total}')

    

  

if __name__ == '__main__':
    transport = PublicTransport(0, 100)
    transport.get_in(20)
    transport.get_in(10)
    transport.get_in(40)
    transport.get_off(30)
    transport.profit() # 탑승인원 : 40 / 총 수익 : 7000
   