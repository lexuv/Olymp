#  2) Stars

#from datetime import datetime
import datetime

N = int(input())
common = datetime.timedelta()
for i in range(N):
    enter = list(input().split())
    a = list(map(int, enter[0].split(':')))
    if a[0] >= 20:
        firstday = 1
    else:
        firstday = 2
    b = list(map(int, enter[1].split(':')))
    if b[0] >= 20:
        secondday = 1
    else:
        secondday = 2
    diff = datetime.datetime(2017, 11, secondday, b[0], b[1]) - datetime.datetime(2017, 11, firstday, a[0], a[1]) 
    common += diff
last = list(map(int, input().split(':')))
if int(last[0]) >= 20:
    firstday = 1
else:
    firstday = 2
remains = datetime.timedelta(hours = 2, minutes = 43) - common
bed = datetime.datetime(2017, 11, firstday, last[0], last[1])
if remains.days >= 0:
    bed += remains
print (bed.strftime("%H:%M"))
