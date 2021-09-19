from collections import deque, defaultdict, Counter

print("** defaultdict: ")
a = 'mississipi'
d = defaultdict(int)
for k in a:
    d[k] += 1

print(dict(d))
print()

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)
print(d)
print()

print("** Counter: ")
c = Counter('abcdaab')
for letter in 'abcde':
    print('%s : %d' % (letter, c[letter]))

