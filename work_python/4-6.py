count=0
i=1


while  i<1001:
    if i%3 != 0: #!= 3의 배수가 아님
        # print(i,end=" ")
        print("%d"%i,end=" ")
        count+=1 #count 1씩증가

        if count%10==0: #10개씩 한줄 만들기
            print()
    i+=1