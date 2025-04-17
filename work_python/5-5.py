numbers = [7,9,15,18,30,-3,7,12,-16,-12]
sum=0
i=0
print("짝수 번째 요소 : ",end=" ")

while i < len(numbers):
    if (i+1)%2 == 0: #짝수일때 0
        sum += numbers[i]  #sum에 리스트값을 i 인덱스값 i를 1씩 증가.
        print(numbers[i],end=" ") # 넘버 인덱스로 숫자 호출
    i+=1 # 들여쓰기 안쪽으로로
print()
print("합계 : ",sum)

