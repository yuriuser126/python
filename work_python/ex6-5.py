area_code = {"서울":"02","부산":"051","대구":"053","광주":"062"}
print(area_code)

for key in area_code:
    print("%s 지역번호 : %s" %(key,area_code[key])) 
    # area_code[key]: 값 키와 값을 순서로 출력