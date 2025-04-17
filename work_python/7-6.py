
def space_hypen (string):
    result=""
    i=0
    # print(len(string))
    while i < len(string):
        if string[i] == " ": # 스페이스바 공백주기
            result+="-"
        else:
            # print(string[i])
            result+=string[i]
        i+=1
    return result


string = input("문자열을 입력하세요 : ")
print( space_hypen(string))