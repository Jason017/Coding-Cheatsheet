Link to [My-Leetcode](https://github.com/Jason017/My-Leetcode) [Algorithm-and-Data-Structure](https://github.com/Jason017/Algorithm-and-Data-Structure)

* ascii character code:
  * 65: A => 90: Z
  * 97: a => 122: z 

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
