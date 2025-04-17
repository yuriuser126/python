phone = input("하이픈(-)을 포함한 휴대폰 번호를 입력하세요 : ")

for x in phone: 
    if x != "-":
        # print(x) # 세로로 쭉 한개씩 내려서 나온다
        # print(x,end=" ") # 가로로 쭉 한개씩 옆으로 나온다
        print("%s"%x,end=" ") # 가로로 쭉 한개씩 옆으로 나온다