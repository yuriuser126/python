#  utf-8 : 세계표준 문자셋(ex) ms949, euc-kr,iso9000번대대)
# f =open("new_file.txt","w", encoding="utf-8") 
# -> #txt를 만들건데 w로  쓰기모드로 가겠다
# f =open("new_file2.txt","w", encoding="utf-8") 
# f =open("new_file3.txt","w", encoding="utf-8") 
f =open("new_file3.txt","a", encoding="utf-8") 
#a 모드 : 기존파일에 내용을 추가가
# names = ["홍지수","안지영","김연수","김예린","한정연"]
names = ["손영민","황현준"]

for name in names:
    f.write(name+"\n") #엔터키 :\n : 줄바꿈꿈
    
# f.write("테스트~")
print("파일 쓰기 완료!")

f.close()