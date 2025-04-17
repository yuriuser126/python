def func(food): #매개변수를 리스트로 받아서 처리가능
    # for x in food:
    #     print(x)
    food.append("딸기")
    food.append("수박")

# func(["사과","오렌지","바나나"]) #대괄호 : 리스트
fruits = ["사과","오렌지","바나나"]  #위와 같다.
# func(fruits)  # 딸기 추가

print(fruits)
func(fruits)  
print(fruits) #함수에서 append 반영되어서 출력