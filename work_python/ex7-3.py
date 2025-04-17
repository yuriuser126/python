def average (*args):
    print(args) # 여러개의 값이 출력이 튜플 형식이다.(85,96,87)
    num_args = len(args) #args의 개수이다 len 사용.
    sum = 0

    for i in range(num_args):
        sum+=args[i]
    # print(sum)
    avg = sum/num_args
    # print(avg)
    print("%d과목평균 : %.1f"%(num_args,avg))

average(85,96,87)
average(77,93,85,97,72)
