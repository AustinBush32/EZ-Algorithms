# l: list to be searched
# x: key 
def binarySearch(l, x): 
    low = 0
    high = len(l)

    while low <= high: 
  
        mid = low + (high - low) // 2; 
          
        # Check if x is present at mid 
        if l[mid] == x: 
            return mid 
  
        # If x is greater, ignore left half 
        elif l[mid] < x: 
            low = mid + 1
  
        # If x is smaller, ignore right half 
        else: 
            high = mid - 1
      
    # If we reach here, then the element 
    # was not present 
    return -1


arr = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(binarySearch(arr, 11))