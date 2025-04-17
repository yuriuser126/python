car = {"brand":"현대","model":"아반떼","start":1990,"year":2021}
print(car)

x = car.pop("start") #pop : 키에 해당되는 값(잘라내기-출력시 사라져있음 ) /
#start키에 해당되는 값 출력력
print(x)

print(car) #"start":1990 사라져 있음

car.clear() # 딕셔너리에 있는 키와 값을 모두 삭제
print(car)