import math
from math import radians
lat1 = 13.0827
lat2 = 9.4533

long1 = 80.2707
long2 = 77.8024

R = 6371
teta1 = radians(lat1)
teta2 = radians(lat2)

teta = radians(lat2 - lat1)
landa = radians(long2 - long1)

a = math.sin(teta/2) * math.sin(teta/2) + math.cos(teta1) * math.cos(teta2) * math.sin(landa/2) * math.sin(landa/2)

c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

d = R * c

print("Distance between two Latitude, Longtitude is : " + str(d))

