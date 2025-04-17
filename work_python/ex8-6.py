class Members:
    total=0 #total - 클래스 속성 공유가능

    # def __init__(self,name): #네임 매개변수를 받음 생성자
    def __init__(self,name,phone): #네임 매개변수를 받음 생성자
        self.name=name #객체네임
        self.phone=phone #객체네임
        # self.total+=1 #카운트 함.
        Members.total+=1 #클래스 속성을 카운트를 함함
    def show_info(self): # 객체 / 오류 :TypeError: Members.__init__() missing 1 required positional argument: 'name'
        # print("이름:%s"%self.name)
        print("이름:%s, 전화번호 :%s"%(self.name,self.phone))

m1 = Members("홍성지","010-3359-3763")
m2 = Members("강동욱","010-1019-4767")
m3 = Members("신진서","010-9018-0298")

m1.show_info()
m2.show_info()
m3.show_info()

# print("총 회원 수 :",m1.total) 
# print("총 회원 수 :",m2.total) 
# print("총 회원 수 :",m3.total) 
print("총 회원 수 :",Members.total) #클래스 속성 ->0이 나옴 count 이용 def init에