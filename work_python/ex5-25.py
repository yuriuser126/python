phone1_list1 = ["010-3654-2637","010-3984-5377","010-3554-0973"]
print(phone1_list1)

phone2_list2= []

for number in phone1_list1:
    # print(number)
    x = number.replace("-","")
    phone2_list2.append(x)  #하이픈 빠진 번호 출력됨

print(phone2_list2) 