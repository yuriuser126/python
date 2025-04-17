num = int(input("수를 입력하세요 : "))

if num >=0 and num <=9 :
    print("%d 은(는) 한자리 숫자이다." %num)
elif num >=10 and num <=99:
    print("%d 은(는) 두자리 숫자이다." %num)
elif num >=100 and num <=999:
    print("%d 은(는) 세자리 숫자이다." %num)
else:
    print("오류! %d 은(는) 범위(0~999) 이외의 숫자이다." % num)