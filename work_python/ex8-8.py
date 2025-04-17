class Person:
    def __init__(self,name):
        self.name=name 
    def show_name(self):
        print(self.name) 
    def show_age(self):
        print(self.age) 

class Student(Person):
    # def __init__(self, name):
    def __init__(self, name,age):
        super().__init__(name) #  super() : 부모클래스에있는 생성자 호출 라는 뜻
        self.age=age

# 오류 :TypeError: Student.__init__() missing 1 required positional argument: 'age'
x = Student("홍길동",20) #나이가 없다
x.show_name()
x.show_age()