import datetime

t1 = datetime.datetime.now()

print(t1.hour)

if (int(t1.hour) > 18):
    print("Night Time")
else:
    print("Day Time")
