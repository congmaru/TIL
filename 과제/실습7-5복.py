import random 

class Students():
    def __init__(self, students):
        self.students = students

    def pick(self,n):
        return random.sample(self.students, n)

    def match_pair(self):
        pair_list = []
        while len(self.students)>0:
            if len(self.students) <=3:
                pair_list.append(self.students)
                break
            else: 
                picked = self.pick(2)
                pair_list.append(picked) #뽑은 두명을 리스트에 넣음
                self.students.remove(picked[0])
                self.students.remove(picked[1])#기존리스트에서 뽑은 두명을 제거
        return pair_list

if __name__ == '__main__':
    students_lst = ['김싸피', '금해피', '테스트', '철수킴', '박영희']
    students = Students(students_lst)
    print(students.match_pair())