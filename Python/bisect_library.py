# https://github.com/Jason017/Algorithm-and-Data-Structure/blob/main/Algorithm/Java/BinarySearch.java
from bisect import bisect_right, bisect_left


def bisectLeft(nums, target):
    # Returns leftmost insertion point that target should be inserted in the sorted array
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left


def bisectRight(nums, target):
    # Returns rightmost insertion point that target should be inserted in the sorted array
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return left


def get_grade(score, cutoffs, grades):
    i = bisect_right(cutoffs, score)
    return grades[i]


cutoffs = [60, 70, 80, 90]
grades = ['F', 'D', 'C', 'B', 'A']
scores = [52, 99, 77, 70, 89, 90, 100]
res = [get_grade(score, cutoffs, grades) for score in scores]
print(res)


# https://www.delftstack.com/howto/python/python-bisect/
# Find the first occurrence of an element
def binary_search(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    else:
        return -1


a = [1, 2, 3, 3, 3]
x = 3
res = binary_search(a, x)
if res == -1:
    print("Element not Found")
else:
    print("First occurrence of", x, "is at index", res)


# Find the greatest value smaller than x
def binary_search(a, x):
    i = bisect_left(a, x)
    if i:
        return (i-1)
    else:
        return -1


a = [1, 2, 4, 4, 8]
x = 7
res = binary_search(a, x)
if res == -1:
    print("There is no value smaller than", x)
else:
    print("Largest value smaller than", x, " is at index", res)


# Find the last occurrence of an element
def binary_search(a, x):
    i = bisect_right(a, x)
    if i != len(a)+1 and a[i-1] == x:
        return (i-1)
    else:
        return -1


a = [1, 2, 4, 4]
x = 4
res = binary_search(a, x)
if res == -1:
    print(x, "is absent")
else:
    print("Last occurrence of", x, "is present at", res)
