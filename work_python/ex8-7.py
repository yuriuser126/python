class Person:
    def __init__(self,name):
        self.name=name #파라미터 받은애를 저장함
    def show_name(self):
        print(self.name) #객체이름 출력

class Student(Person): #person을 상속받는 student 클래스 / person 부모 student 자식클래스
    pass

#오류 :TypeError: Person.__init__() missing 1 required positional argument: 'name'
x = Student("홍길동") #학생 객체생성 x로 받음 / 학생객체에 이름이 없다.->직접적어줌
x.show_name()