import colcon as c
from pprint import pprint

result = []
for i in range(100, 10000):
    r = []
    j = i
    while j >= 2:
        j = c.isoddeven(j)
        r.append(j)
    result.append(r)
pprint(result)
