class Student:
    # pet=[] #[] : 리스트 -> 클래스 속성임 / ex) 한집에 존, 샐리 삼 펫을키우면 강아지,고양이 같이 다님
    def __init__(self): #생성자자
        self.pet=[] #객체에 해당되는 펫.
    def push_pet(self,x): #강아지나 고양이를 x로 받는다 
        self.pet.append(x) #append로 리스트 추가하겟다

john = Student() #객체 생성 학생 john:학생이름 참조변수
john.push_pet("고양이") #고양이 리스트형식 / 객체.매소드 호출 
print(john.pet) #리스트 속성.

sally = Student() 
sally.push_pet("이구아나") 
# print(sally.pet) #['고양이', '이구아나']-> 클래스 속성이라서 객체들이 다 공유됨
print(sally.pet) #[ '이구아나']-> 객체 속성이라서 공유지 않음.