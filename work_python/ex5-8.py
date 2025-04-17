scores=[] #딜리스트 안에 내용 없는 리스트

while True:
    # score = input("성적을 입력하세요(종료:-1):") #문자와 숫자비교하면 무한루프
    score = int(input("성적을 입력하세요(종료:-1):"))

    if score == -1:
        break
    else:
        scores.append(score)

print(scores)