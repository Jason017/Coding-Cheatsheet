# My Python Cheatsheet

* built-in functions sort in python
  * list.sort(): O(Nlog(N)) O(1)
  * sorted(list): O(Nlog(N)) O(log(N))

* ascii character code:
  * 65: A => 90: Z
  * 97: a => 122: z
  * ord('a') = 97
  * chr(97) = 'a'

* list[start:stop:step]
  1. start: index to start, inclusive (defaults to 0)
  2. stop:  index to stop,  exclusive (defaults to len)
  3. step:  slice by step             (defaults to 1)

  * Same as list[slice(start,stop,step)]
    * [1, 2, 3][:]    → [1, 2, 3]
    * [1, 2, 3][::2]  → [1, 3]
    * [1, 2, 3][:1]   → [1]
    * [1, 2, 3][1:]   → [2, 3]
    * [1, 2, 3][::-1]   → [3, 2, 1]

  * negative indexes wrap
    * nums = list(range(0, 11))   11 elements
    * nums[-5:]     → [6, 7, 8, 9, 10]
    * nums[-5:10]   → [6, 7, 8, 9]
    * nums[:-2]     → [0, 1, 2, 3, 4, 5, 6, 7, 8]
    * nums[2:-2]    → [2, 3, 4, 5, 6, 7, 8]

* [Time Complexity of Data Structure in Python](https://wiki.python.org/moin/TimeComplexity)
* [Complexity of Python Operations](https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt)
* [Algorithm-and-Data-Structure](https://github.com/Jason017/Algorithm-and-Data-Structure)

* [My-Leetcode](https://github.com/Jason017/My-Leetcode)
* [My-Interview-Questions](https://github.com/Jason017/SWE-Interview-Question-Collection)
* [My-Mock-Interview-Questions](https://github.com/Jason017/SWE-Interview-Question-Collection/tree/main/My-Mock-Interview)
