sentence = input("문장을 입력해 주주세요 : ")
i = len(sentence) - 1  # i>=0 를 해서 len길이에서 -1을함 aaa>3개 i 로 돌리면 4번돔
# 문장 전체길이

#에서 감소되는걸 찾아야함.
while i>=0: 
    if sentence[i]==" ": #공백일때니까 스페이스 쳐놔야함
        print("-",end="") 
        #조건 먼저 공백일때 - 나오게
    else:
        print(sentence[i],end="") #역방향
        print("%s " %sentence[i],end="") #역방향
    i-=1


