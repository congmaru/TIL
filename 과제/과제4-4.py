words = ["eat", "tea", "tan", "ate", "nat", "bat"]

anagram_dict = {}  # 애너그램단위로 묶은 결과가 들어있는 딕셔너리
# key : 해당 단어를 정렬한 결과
# value : key와 같은 애너그램 그룹에 있는 단어들의 모음을 리스트로 만든다.

for word in words:
    sorted_word = "".join(sorted(word))  # sorted() => 결과가 리스트, 문자열로 변환해야한다. ==> join()
    # word = "eat"
    # sorted(word) = ["a" , "e" , "t"]
    # "".join(sorted(word)) = "aet"
    # ".".join(sorted(word)) = "a.e.t"
    print(sorted_word)
    if anagram_dict.get(sorted_word):  # 딕셔너리에 애너그램 그룹이 존재한다.
        anagram_dict[sorted_word].append(word)  # 존재하면 리스트에 추가를 해준다.
    else:
        anagram_dict[sorted_word] = [word]  # 존재하지 않으면 리스트를 새로 만들어준다.

print(anagram_dict)