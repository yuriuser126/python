class Person: #사람이나 사물이 될수 있는 틀 / 판 ->붕어빵판판
    name = "김정연" # name: 속성
    #person1 객체를 self가 받음!!
    def hello(self): # self : hello 메소드 호출될때 객체를 self가 받는다. hello: 기능능
        # print("안녕하세요")
        print(Person.name + "님 안녕하세요") #클래스.속성 사용함.

person1 = Person() #객체 생성한다. (사람을 만든격) / person1 :이름,참조변수이다
person1.hello() # 메소드 호출

Person.name="황서영"
person1.hello() #메소드 호출 -> 황서영 나옴