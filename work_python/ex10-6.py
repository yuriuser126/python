import os

if os.path.exists("test"): #test 폴더가 존재하는가?
    os.rmdir("test") #폴더삭제제
else:
    print("폴더가 존재하지 않음!")