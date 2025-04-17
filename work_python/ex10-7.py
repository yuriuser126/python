import csv

file_name = "weather.csv"
f = open(file_name,"r",encoding="utf-8")
lines = csv.reader(f) #csv.reader(f) : CSV 파일 전체를 읽어옴. lines

for line in lines:
    print(line) #라인별로 읽어온다 -

f.close()