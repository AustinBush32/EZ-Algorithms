""" 
l: List to be sorted
left: Left most index
right: right most index
"""
def quicksort(l, left, right):
	if (left < right): 
		"""
		We divide the list into sublists around the pivot index. This is the divide
		and conquer phase of the algorithm, the real work of the sort is done in
		partition method, so there is nothing else to do here.
		"""
		pIndex = partition(l, left, right)
		quicksort(l, left, pIndex-1)
		quicksort(l, pIndex+1, right)

"""
This function takes middle element as pivot, places 
the pivot element at its correct position in the sorted 
list, and places all smaller elements to left of 
pivot and all greater elements to right of pivot

l: List to be partitioned
left: Left most index
right: Right most index
"""
def partition(l, left, right):
	pivotIndex = (right-left)//2 + left
	pivot = l[pivotIndex] 
	swap(l, pivotIndex, right) #move pivot to the end of the sublist
	p = left #p will become the final index of the pivot.
	for i in range(left, right):
		if l[i] < pivot:
			"""
			if the element at index i is less than the pivot than swap that element
			with the left most open spot.
			"""
			swap(l, i, p)
			p += 1
	swap(l, p, right) #move the pivot to its correct location
	return p

""" 
l: List
a: First element to swap
b: Second element to swap
"""
def swap(l, a, b):
	l[b], l[a] = l[a], l[b]

l = [1, 10, 2, 5]
quicksort(l, 0, len(l)-1)
print(l)