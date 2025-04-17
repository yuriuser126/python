sum =0
i=500

while i<=600: # 5의배수를 누적
    if i%5 ==0:
        sum += i
    i+=1
print("5의 배수의 합계 : %d"%sum)