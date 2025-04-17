# 함수 : 없음, 반환값 : 없음, 매개변수 : 없음
# def hello():
# name : 함수안에서 사용시 색깔이 진하게 변함, 원래 연한 하늘색임임
# def say_hello(name): #name : 매개변수,파라미터, 아규먼트,인자값
def say_hello(first_name,last_name): 
    # print("안녕하세요!")
    # print("%s  님 안녕하세요!"%name)
    name = first_name + last_name
    print("이름",name)

# 함수 호출
# hello()
# hello()
# hello()
# say_hello("") #오류 :TypeError: say_hello() missing 1 required positional argument: 'name' -> 매개변수 name 안받음음
# say_hello("홍지수") 
# say_hello("안지영") 
# say_hello("황예린") 
say_hello("정원","홍") 
