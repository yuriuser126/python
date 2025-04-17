number = input("숫자를 입력하세요 : ")
count = 0

# for a in (number):
#     if  i== "1" or i== "3" or i== "5" or i== "7" or i== "9" :
#         count+=1
# print("홀수의 개수  : %d개" %count)

for a in (number):
    a = int(a) #int 로 지정안하면 오류남. 숫자형으로.

    if a%2==1:
        count+=1
print("홀수의 개수  : %d개" %count)

# for a in range(number): # 오류 :TypeError: 'str' object cannot be interpreted as an integer
#     print(a)
#     print(number)

# for a in range(int(number)):#5 입력
#     print(a) #0 1 2 3 4 
#     print(number) #5출력

# for a in number: #5 입력
#     print(a) #5를받음
#     print(number) #5를 받음