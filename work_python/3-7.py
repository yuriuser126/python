char2 = input("영문 대문자 또는 소문자 하나를 입력하세요 : ")


char = char2.upper()

if  char =="A"  or  char=="E" or char=="I" or  char=="O"or  char=="U":
    print("%s -> 모음")
else:
    print("%s -> 자음")
