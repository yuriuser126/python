aninmals = ("토끼","거북이","사자","여우")
print(aninmals)

#오류발생 -> TypeError : 'tuple' object does not support item
#튜플에서 변경 불가
# animals  [2]="호랑이"
# print(aninmals)

# numbers = tuple(range(10))
# print(numbers)
n=tuple(range(10,21)) #10에서 21전까지
print(n)

print("n[0]=" ,n[0]) #인덱스 0번
print("n[2:5]=" ,n[2:5]) #인덱스 2에서 4까지
print("n[2:]=" ,n[2:]) #인덱스 2에서 끝까지
print("n[:5]=" ,n[:5]) # 인덱스 4까지
print("n[-2]=" ,n[-2]) #뒤에서 두번째
print("n[::-1]=" ,n[::-1]) #::-1 =>맨뒤에서 맨앞으로 출력