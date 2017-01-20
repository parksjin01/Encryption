import random
from pandas import DataFrame
res = []
s1 = [0, 0, 0, 0, 0, 0, 0]
s2 = []
for i in range(53):
    tmp1 = [1, 1, 1, 1, 1, 1]
    tmp2 = []
    while(2560000>sum(tmp1) or sum(tmp1)>2580000):
        tmp1 = []
        for _ in range(6):
            tmp1.append(random.randrange(370000, 480000, 10))
    tmp1.append(sum(tmp1))
    for num in tmp1:
        tmp2.append("{:,}".format(num))
    res.append(tmp2)
    for idx in range(7):
        s1[idx] += tmp1[idx]
for num in s1:
    s2.append("{:,}".format(num))
res.append(s2)
df = DataFrame(res)
print df
print res
df.to_excel('mama.xlsx')
