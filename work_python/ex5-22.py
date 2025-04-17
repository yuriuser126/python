hello="have a nice day"
print(hello)

list1 = hello.split(" ")
print(list1)
print(type(list1)) #리스트 타입이다를 알려준다. 타입을 알려준다.
#문자열을 스플릿 쪼갯을때 리스트로 저장한다.

for i in range(0,len(list1)):
    print("list1[%d] : %s"%(i,list1[i]))
    
