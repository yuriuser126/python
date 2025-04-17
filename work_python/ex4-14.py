s = "Python is widely used by a number of big companies"
i=0
count =0

print("모음 : ")

while i<=len(s)-1 : #len () -> 문자열 길이 / i가 0부터라 -i 해주던지 <= 이걸 < 이거로 바꾸던가 
    if (s[i] == "a" or s[i] == "A" or s[i] == "e" or s[i] == "E"
        or s[i] == "i" or s[i] == "I" or s[i] == "o" or s[i] == "O"
        or s[i] == "u" or s[i] == "U"):
        count+=1
        print(s[i],end=" ")
    i+=1 #들여쓰기 해야함

print()
print("모음개수 : %d" %count)