import heapq

arr = [3,1,4,9,7,5]
heapq.heapify(arr)
heapq.heappushpop(arr, 2) # Heappush and heappop and return the smallest element
heapq.heapreplace(arr, 0) # Pop and return the smallest element and add a new item
print(arr)

heapq.heappush(arr, 6) # Insert an element into the heap
print(heapq.nlargest(2, arr)) # return top 2 elements of the heap
print(heapq.nsmallest(2, arr)) # return last 2 elements of the heap
print(arr[0]) # Get the smallest element of the heap
heapq.heappop(arr) # Delete the smallest element of the heap
print(arr)


# Heap method	            Time complexity	    Space complexity
# 
# Construct a Heap	        O(N)	            O(N)
# Insert an element	        O(logN)     	    O(1)
# Get the top element	    O(1)    	        O(1)
# Delete the top element	O(log N)	        O(1)
# Get the size of a Heap	O(1)     	        O(1)