person = {"name":"홍길동","age":30,"family":5,"children":["선미","성진","소영"],"pets":["강아지","고양이","이구아나"]}

for key in person:
    # print(key)
    if key == "children":
        # print(person[key])
        # print(len(person[key]))
        num_child = len(person[key])
        print("자녀수 : %d명" %num_child)
