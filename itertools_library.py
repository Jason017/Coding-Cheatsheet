import itertools

counter = itertools.count()

data=[500,150,350,450]
daily_data = list(zip(itertools.count(),data))
print(daily_data)
daily_data = list(itertools.zip_longest(range(10),data))
print(daily_data)


squares = map(pow, range(10), itertools.repeat(2))
starSquares = itertools.starmap(pow, [(0,2), (1,2), (2,2)])
print(list(squares))
print(list(starSquares))