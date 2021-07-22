from collections import deque, defaultdict, Counter

a = 'mississipi'
d = defaultdict(int)
for k in a:
    d[k] += 1

print(d)
