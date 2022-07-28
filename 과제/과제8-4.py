
class Stack:
    #인스턴스가 생성될 때 빈 리스트를 각 인스턴스 이름공간에 넣는다.
    def __init__(self):
        self.stk = []  #인스턴스변수로 빈 리스트를 만들어라
        
    #스택이 비었다면 True, 그렇지 않으면 False 반환
    def empty(self):
        if self.stk == []:
            return True
        return False
        # return True if self.stk ==[] else False// 삼항연산자
        
    #스택의 가장 마지막 데이터 반환. 스택이 비었다면 None 반환
    def top(self):
        flag = self.empty()
        if flag == True:
            return None
        return self.stk[-1]

        # return self.stk[-1] if self.empty() is not True else None

    #스택의 가장 마지막 데이터값을 반환하고, 해당 데이터 삭제
    #스택이 비었다면 None반환
    def pop(self):
        flag = self.empty()
        if flag == True:
            return None
        #리스트의 함수 중 삭제+반환을 동시에 해주는 함수 pop()
        return self.skt.pop(len(self.stk)-1)
        return self.skt.pop(len(self.stk)-1) if self.empty() is not True else None
        # return None if self.empty() else self.data.pop(len(self.data)-1)
        

    #스택의 가장 마지막 데이터 뒤에 값 추가. 반환값은 없음.
    def push(self):
        self.stk.append(stk)

    #스택의 현재 요소들들을 보여줌(반드시 문자열 반환)
    def __repr__(self):
         return f'{self.data}'

stack = Stack()
print(stack.empty())


# #_________________________________

# class Stack:
#     def __init__(self): #생성자. stk =  []을 선언함
#         self.stk=[]

#     def __str__(self):
#         return str(self.stk[::1])
    
#     def empty(self):
#         return len(self.stk)==0
    
#     def top(self):
#         if not self.empty():
#             return self.stk[-1]
#         else:
#             return "None"
        
    
#     def pop(self):
#         if not self.empty():
#             return self.stk.pop(-1)
#         else:
#             return "None"
    
#     def push(self,data):
#         self.stk.append(data)      

#     def __repr__(self):
#         return self.stk

# stack=Stack()


# stack.push(1)
# print(stack)
