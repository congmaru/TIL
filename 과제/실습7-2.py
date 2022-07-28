class Wordrelay():
<<<<<<< HEAD
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
=======
        def __init__(self, words):
                self.words = words

        def check_fail(self):
                past_words = [self.words[0]]
                if len(self.words) == 1:
                        return -1
                for i in range(1, len(self.words)):
                        if self.words[i] == 'done':
                                return -1
                        if self.words[i][0] != past_words[-1][-1]:
                                return i + 1
                        elif self.words[i] in past_words:
                                return i + 1
                        past_words.append(self.words[i])

        def get_result(self):
                result = self.check_fail()
                if result == -1:
                        return '탈락한 사람이 없다'
                else:
                        return f'{result}번 째 사람이 탈락하였습니다.'


if __name__ == '__main__': #다른 파일에서 위의 모듈을 불러올 때 이 아래로는 보이지 않기 위한 명령어 
        words = ["round","dream","magnet","tweet","tweet","trick","kiwi"]
        wordrelay = Wordrelay(words)
        print(wordrelay.get_result())
>>>>>>> c4222d6c1fb6829074ccd5f94fdb7c6397e66662
