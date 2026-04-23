import sys
import math
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    last = {}  # dictionary instead of fixed array
    
    for i in range(n):
        ans = -1
        
        for v in last:
            if math.gcd(arr[i], v) == 1:
                ans = max(ans, last[v])
        
        print(ans, end=" ")
        last[arr[i]] = i
    
    print()
