class Wordrelay():
    # 1. words 리스트를 전달받아 인스턴스 변수로 만드는 생성자를 구현하세요
    # def __init__(self ~~~~ )
    def __init__(self,words):

    # 2. 실패와 성공 여부를 결하는 함수를 구현하세요
    def check_fail(self):
        pass
    
    # 3. 결과를 돌려주는 함수를 작성하세요.
    def get_result(self):
        pass


if __name__ == '__main__':
    words = ["round","dream","magnet","tweet","tweet","trick","kiwi"]
    wordrelay = Wordrelay(words)
    print(wordrelay.get_result()) # 5번째 참가자가 탈락하였습니다.