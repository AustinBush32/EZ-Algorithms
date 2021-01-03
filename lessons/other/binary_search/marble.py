import sys

def binarySearch(l, low, high, x):

    while low <= high: 
  
        mid = low + (high - low) // 2; 
           
        if l[mid] == x: 
            return mid 
  
        elif l[mid] < x: 
            low = mid + 1
  
        else: 
            high = mid - 1

    return -1

lines = sys.stdin.readlines()
case = 0
i = 0

while lines[i].strip() != '0 0':
    case+=1
    sys.stdout.write(f"CASE# {case}:\n")
    line = lines[i].split()
    n = int(line[0])
    q = int(line[1])

    marbles = list(map(int, lines[i+1:i+n+1]))
    queries = list(map(int, lines[i+n+1:i+n+q+1]))

    i = i + n + q + 1

    marbles.sort()

    for j in queries:
        high = len(marbles) - 1
        ans = -1
        while True:
            index = binarySearch(marbles, 0, high, j)
            if index != -1:
                ans = index
                high = index - 1
            elif index == -1:
                if ans == -1: 
                    sys.stdout.write(f"{j} not found\n")
                    break
                else:
                    sys.stdout.write(f"{j} found at {ans+1}\n")
                    break


