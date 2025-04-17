data = [10,20,30,40,50,60,70,80]
print(data)

# x = data.pop() 
#마지막거 나온다. pop()파라미터가 없으면마지막값이나옴
x = data.pop(2) 
# 30이 나온다 인덱스에 있는 아이를 잘라내겠다. 파라미터가 해당인덱스의 값을 잘라내기
print(x)
print(data)

x = data.pop(3) 
print(x)
print(data)