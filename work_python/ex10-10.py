import json

# load : json 파일을 디코딩해서 딕셔너리로 저장함
# with open("member.json","w",encoding="utf-8") as f:
with open("member.json","r",encoding="utf-8") as f:
    dict = json.load(f)

    print(dict)
