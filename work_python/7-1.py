def km_to_mile (x): # 안에 x를 줘서 걔산
    result = x * 0.621371
    return result # 리턴값 주기

km = int(input("킬로미터를 입력하세요 : "))
mile = km_to_mile(km) # 함수 결과값 마일로 정의
print("%d킬로미터는 %.2f 마일 이다." %(km,mile)) # 프린트로 출력