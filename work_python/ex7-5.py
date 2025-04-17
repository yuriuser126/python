# def func(n): #리턴값이 없을 때 none 
def func(): #매개변수뺏을때때
    # x=n+5
    # return x
    global x
    x=100 # 지역변수 : 함수 내에서만 사용가능 
    print(x)

# a=func(10)
# print(a)
# b=func(20)
# print(b)
# func()
# print(x) # 전역변수 x 가 없어서 오류 #오류 :NameError: name 'x' is not defined
x=200 #200은 밖에서만 작용한다.
print(x) 
func()
print(x) 
#global x 적용후 바뀜 x=200을 x=100으로 바꿔치기함
# 200 -> 200
# 100 -> 100
# 200 -> 100
