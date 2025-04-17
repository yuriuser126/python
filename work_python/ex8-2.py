class Cat:
    # 속성 : 3개
    kor_name="로키" #kor_name : 속성 - 클래스의 속성
    eng_name="rocky" #eng_name : 속성
    age=2 #age : 속성

    def sound(self): #메소드 기능 : 소리 / def+self 세트
        print("야옹~~~")
    def speed(self): 
        print("엄청빠르다!")

mycat = Cat() #객체 생성 mycat:이름 mycat객체 생성
print("한글이름 :",mycat.kor_name) # 객체의 속성으로 출력
print("영어 이름 :",mycat.eng_name) 
print("나이 :",mycat.age) 
mycat.sound() #객체의 메소드로 호출해서 출력함. 객체.매소드
mycat.speed() #객체의 메소드로 호출해서 출력함. 객체.매소드