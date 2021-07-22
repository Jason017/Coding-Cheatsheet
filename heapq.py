import heapq

arr = [3,1,4,9,7,5]
heapq.heapify(arr)
heapq.heappushpop(arr, 50)
heapq.heapreplace(arr, 0)
print(arr)
