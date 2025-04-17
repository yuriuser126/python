def cir_area():
    result=r*r*3.14
    return result

def cir_len():
    result=2*3.14*r
    return result

# r=10
r = int(input("반지름을 입력하세요:"))
area = cir_area()
# area = cir_area(r) #오류 : TypeError: cir_area() takes 0 positional arguments but 1 was given 매개변수 r 제공된거 없는데 1개 제공됫다고 함.
length= cir_len()
print("원의면적:%.1f ,원주의 길이:%.1f"%(area,length))