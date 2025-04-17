string = input("문자열을 입력하세요 : ")

num_string =len(string) 


if num_string % 2==0:
    print("문자열의 개수 : %d" %num_string)
    print("문자열의 개수는 짝수이다." )
else:
    print("문자열의 개수 : %d" %num_string)
    print("문자열의 개수는 홀수이다." )

