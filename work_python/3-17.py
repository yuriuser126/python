print("기능선택")
print("1. 더하기")
print("2. 빼기")
print("3. 곱하기")
print("4. 나누기")

x = input("계산기 기능을 선택하세요(1/2/3/4) : ")

num1 = int(input("첫 번째 숫자를 입력하세요 : "))
num2 = int(input("두 번째 숫자를 입력하세요 : "))

if x =="1":
    print( "%d + %d = %d" %(num1,num2,num1+num2))
elif x =="2":
    print( "%d - %d = %d" %(num1,num2,num1-num2))
elif x =="3":
    print( "%d * %d = %d" %(num1,num2,num1*num2))
elif x =="4":
    print( "%d / %d = %d" %(num1,num2,num1/num2))
else:
    print("입력 숫자가 잘못되었습니다!")