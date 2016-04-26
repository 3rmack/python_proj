import datetime

y, m, d = (int(n) for n in input().split())
day_offset = datetime.timedelta(days=int(input()))
day = datetime.date(y, m, d)
day_result = day + day_offset
print(day_result.year, day_result.month, day_result.day)
