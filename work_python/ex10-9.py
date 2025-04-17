import json

member = {"id":"swhong",
 "name":"홍성우",
 "age":23,
 "history":[
     {"date":"2021-03-15","route":"mobile"},
     {"date":"2020-06-23","route":"pc"}
 ]
 }

# dump() : 딕셔너리를 json 파일로 생성
with open("member.json","w",encoding="utf-8") as f:
    # json.dumps(member,f,ensure_ascii=False,indent=4)
    json.dump(member,f,ensure_ascii=False,indent=4)
