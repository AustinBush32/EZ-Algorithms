import sys
import math

def quicksort(l, left, right):
	if (left < right): 
		pIndex = partition(l, left, right)
		quicksort(l, left, pIndex-1)
		quicksort(l, pIndex+1, right)

def partition(l, left, right):
	pivotIndex = (right-left)//2 + left
	pivot = l[pivotIndex] 
	swap(l, pivotIndex, right)
	p = left
	for i in range(left, right):
		if l[i] < pivot:
			swap(l, i, p)
			p += 1
	swap(l, p, right)
	return p

def swap(l, a, b):
	l[b], l[a] = l[a], l[b]

n = int(sys.stdin.readline())

for i in range(n):
	line = list(map(int, sys.stdin.readline().strip().split(" ")))
	g = list()
	cookies_eaten = line[0] - line[1]
	if cookies_eaten == 0: 
		sys.stdout.write(f"Case #{i+1}: 0\n")
	else:
		for q in range(1, int(math.sqrt(cookies_eaten)) + 1):
			if cookies_eaten%q == 0:
				if q > line[1]:
					g.append(q)
				if cookies_eaten//q != q:
					if cookies_eaten//q > line[1]:
						g.append(cookies_eaten//q)
		quicksort(g, 0, len(g)-1)
		sys.stdout.write(f"Case #{i+1}: {' '.join(map(str, g))}\n")
