from datetime import datetime

def time_delta(t1, t2):
    format = "%a %d %b %Y %H:%M:%S %z"
    time1 = datetime.strptime(t1, format)
    time2 = datetime.strptime(t2, format)
    return str(abs(int((time1 - time2).total_seconds())))

for _ in range(int(input())):
    t1 = input()
    t2 = input()
    print(time_delta(t1, t2))
