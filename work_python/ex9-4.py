import time

seconds = time.time()
#1739245458.0555902
print(seconds) #그리니치 천문대 기준으로 1970년 1월 1일 0시 0분 0초부터 경과된 시간(밀리세컨드)

tm = time.gmtime()
#time.struct_time(tm_year=2025, tm_mon=2, tm_mday=11, tm_hour=3, tm_min=44, tm_sec=18, tm_wday=1, tm_yday=42, tm_isdst=0)
print(tm) 

tm2 = time.localtime(1739245458.0555902)
print("년:",tm2.tm_year) #2025 출력됨
print("월:",tm2.tm_mon) 
print("일:",tm2.tm_mday) 
print("시:",tm2.tm_hour)
print("분:",tm2.tm_min)
print("초:",tm2.tm_sec) 

# tmmm = time.ctime()
# print(tmmm) 