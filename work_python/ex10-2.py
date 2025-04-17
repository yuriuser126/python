f =open("new_file3.txt","r", encoding="utf-8") #r : 읽기모드
lines = f.readlines()  #readlines : 전체내용을 읽어옴

for line in lines:
    temp = line.replace("\n","")
    print(temp)

# print(lines)
print("파일 읽기 완료!")

f.close()