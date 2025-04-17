class Members:
    def __init__(self): #__init__ : 생성자
        pass #pass : 동작없이 다음실행 _ 의미없음 
    def set_info(self,name):
        self.name=name #self.name : 객체의 속성이다.
        # print(name) #홍지수 출력됨
    def show_info(self):
        print("이름:",self.name) #self.name ->메소드가 바뀌어서 이렇게 입력해야 네임 인식함 

member1 = Members() #객체생성 member1 :이름 참조변수
member1.set_info("홍지수") #self는 객체고 name이름은 만든다.
member1.show_info()

member2 = Members() #객체생성 member2 :이름 참조변수 / 사람 두명 만듬
member2.set_info("안지영") #self는 객체고 name이름은 만든다.
member2.show_info()