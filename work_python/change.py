price=3000
num=3
pay=10000

change=pay-price*num
# print(change)
# print("거스름돈--> 원"change) #오류
# print("거스름돈--> 원"%change)  #오류
print("거스름돈--> %d원"%change) #change 변수를 %d로 받음(정수)
print("거스름돈--> %f원"%change) #change 변수를 %f로 받음(실수-소숫점)