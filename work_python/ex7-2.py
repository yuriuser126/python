def even_odd(n):
    if n%2 == 0: #오류 : TypeError: not all arguments converted during string formatting
        print("%d은(는) 짝수이다" %n)
    else:
        print("%d은(는) 홀수이다" %n)

# even_odd(7)
# x = input("양의 정수를 입력하세요: ") #오류 : TypeError: not all arguments converted during string formatting
x = int(input("양의 정수를 입력하세요: ") )
even_odd(x)
