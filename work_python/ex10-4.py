f =open("scores.txt","r", encoding="utf-8") 
lines = f.readlines()  

# for반복문
for line in lines:
    data = line.split()
    i=0
    sum=0

    #while 반복문
    while i<len(data):
        if i == 0:
            # print(data[i])
            print(data[i],end=" : ")
        else:
            #오류 :TypeError: unsupported operand type(s) for +=: 'int' and 'str'
            # sum+=data[i] # 아니라면 점수 누적
            sum+=int(data[i]) # int형식으로 바꿈
        i+=1 
    # avg = sum/5
    avg = sum/(len(data)-1)
    # print(avg)
    print("%.1f점"%avg)

        #while 문이 끝나면 평균을 출력하겠다.
print("파일 읽기 완료!")

f.close()