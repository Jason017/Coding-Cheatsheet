import itertools

counter = itertools.count()

# zip
data=[500,150,350,450]
daily_data = list(zip(range(len(data)),data))
print(daily_data)
daily_data = list(itertools.zip_longest(range(10),data))
print(daily_data)


# starmap
squares = map(pow, range(10), itertools.repeat(2))
starSquares = itertools.starmap(pow, [(0,2), (1,2), (2,2)])
print(list(squares))
print(list(starSquares))


# permutations
s=['a','b','c']
perm = list(itertools.permutations(s, len(s)))
print('perm:', perm)

perm_all = []
for i in range(len(s)):
    for p in list(itertools.permutations(s, i)):
        if p:
            perm_all.append(list(p))
print('all perm:',perm_all)


# combinations
s=['a','b','c']
comb = [''.join(i) for i in itertools.combinations(s, 2)]
print('comb:',comb)
