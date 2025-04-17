import os
# if os.path.exists("scores3.txt"):
#     os.remove("scores3.txt")

if os.path.exists("scores2.txt"): #scores2.txt 존재하는가?
    os.remove("scores2.txt") #scores2.txt 삭제함 참이면
else:
    print("파일이 존재하지 않음!")