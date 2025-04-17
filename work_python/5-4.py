numbers = [7,9,15,18,30,-3,7,12,-16,-12]
sum=0
i=0

# for number in numbers:
#      sum += number
while i < len(numbers):
    sum += numbers[i]  #sum에 리스트값을 i 인덱스값 i를 1씩 증가.
    i+=1
print("합계 : ",sum)