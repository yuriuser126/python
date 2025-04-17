class Members:
    def __init__(self, name, age): #__init__ : 생성자 한번만 호출함
        # pass #pass : 동작없이 다음실행 _ 의미없음 
        self.name=name #객체의 이름은 매개변수
        self.age=age #객체의 나이는 매개변수
    def show_info(self):
        # print("이름:",self.name) #오류 :AttributeError: 'Members' object has no attribute 'name' 
        print("이름:",self.name) 
        print("나이:",self.age) 
        print()

# 객체 생성->생성자 호출 =>def __init__(self, name, age): -> 매개변수가 안맞으면오류
member1 = Members("황선영",18) #출력이 됨. show_info 에 속성 두개없어서 입력함. 
# member1 = Members() # 오류 :TypeError: Members.__init__() missing 2 required positional arguments: 'name' and 'age'
member1.show_info()

member2 = Members("최종화",32) #출력이 됨. show_info 에 속성 두개없어서 입력함. 
member2.show_info()
