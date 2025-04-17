with open("new_file3.txt","r", encoding="utf-8") as f: 
#별칭을 f
    for line in f:
        temp = line.replace("\n","")
        print(temp)

print("파일 읽기 완료!")

f.close()