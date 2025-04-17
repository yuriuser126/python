member = {"name":"황예린","age":"22","email":"yerin@ganmail.net"}
print(member)

score = dict([("국어",80),("영어",90),("수학",100)]) #대괄호 리스트 중괄호 딕셔너리 소괄호 튜플플
print(score) # 리스트,튜플을 사용해서 딕셔너리를 생성  딕셔너리 형태로 출력됨
print(score["국어"]) # 키를 사용해서 값을 출력했다.
print(score["영어"]) 
print(score["수학"]) 

score["음악"]=70 #없는키는 추가
print(score)

score["수학"]=77 # 있는키는 값을 변경
print(score)

