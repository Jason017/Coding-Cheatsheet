from collections import deque, defaultdict, Counter


print("** defaultdict: ")
a = 'mississipi'
d = defaultdict(int)
for k in a:
    d[k] += 1

print(dict(d))
print()


print("** Counter: ")
c = Counter('abcdaab')
for letter in 'abcde':
    print('%s : %d' % (letter, c[letter]))
print()
