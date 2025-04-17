n=1
sum=0
count=0

while n<=100:
    if n%2==1: #홀수 일때
        sum += n # 합계 누적 홀수 sum= sum+n
        print("%6d"%sum,end=" ") #6칸 빈칸+합계 +스페이스
        count+=1 # 도는 카운트

        if count%10==0: # 10번돌때 
            print() # 엔터 정리리
    n+=1