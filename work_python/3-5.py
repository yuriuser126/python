num1= int(input("첫 번째 정수는?"))
num2= int(input("두 번째 정수는?"))
num3 = int(input("세 번째 정수는?"))


if num1 > num2 and num1 > num3:
    largest = num1
elif num1 > num2 and num2 > num3:
    largest = num2
else:
    largest = num3

print("%d, %d, %d 중에서 가장 큰 수는 %d 입니다." %(num1,num2,num3,largest))
# if a < b and b < c:
#         print("%d,%d,%d 중에서 가장 큰 수는 %d입니다." %(a,b,c))
# if a < c and c < b:
#         print("%d,%d,%d 중에서 가장 큰 수는 %d입니다." %(a,c,b))
# if b < a and a < c:
#         print("%s,%s,%s 중에서 가장 큰 수는 %d입니다." %(b,a,c,c))
   
