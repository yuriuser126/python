x = int(input("정수를 입력하세요 :"))

if x%2== 0:
    print("짝수이다!")
    # else # 오류 :SyntaxError: invalid syntax
# else: 콜론 붙이는 순간 알아서 들여쓰기 됨
else :
    print("홀수이다!")