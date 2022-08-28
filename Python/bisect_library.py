import bisect

def get_grade(score, cutoffs=[60, 70, 80, 90], grades = ['F','D','C','B','A']):
    i = bisect.bisect_right(cutoffs, score)
    return grades[i]

grades = [get_grade(score) for score in [52, 99, 77, 70, 89, 90, 100]]
print(grades)



# https://www.delftstack.com/howto/python/python-bisect/

### Find the first occurrence of an element
from bisect import bisect_left 
 
def binary_search(a, x): 
    i = bisect_left(a, x) 
    if i != len(a) and a[i] == x: 
        return i 
    else: 
        return -1
 
a  = [1, 2, 3, 3, 3] 
x = 3
res = binary_search(a, x) 
if res == -1: 
    print("Element not Found") 
else: 
    print("First occurrence of", x, "is at index", res)


### Find the greatest value smaller than x
def binary_search(a, x): 
    i = bisect_left(a, x) 
    if i: 
        return (i-1) 
    else: 
        return -1
  
a  = [1, 2, 4, 4, 8] 
x = 7
res = binary_search(a, x) 
if res == -1: 
    print("There is no value smaller than", x) 
else: 
    print("Largest value smaller than", x, " is at index", res) 


### Find the last occurrence of an element
from bisect import bisect_right 
  
def binary_search(a, x): 
    i = bisect_right(a, x) 
    if i != len(a)+1 and a[i-1] == x: 
        return (i-1) 
    else: 
        return -1

a  = [1, 2, 4, 4] 
x = 4
res = binary_search(a, x) 
if res == -1: 
    print(x, "is absent") 
else: 
    print("Last occurrence of", x, "is present at", res) 



