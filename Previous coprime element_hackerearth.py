import sys
input = sys.stdin.read
def solve():
    data = input().split()
    if not data:
        return
    
    idx = 0
    T_str = data[idx]
    idx += 1
    T = int(T_str)
    MAX_V = 1001
    coprimes = [[] for _ in range(MAX_V)]
  
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    for i in range(1, MAX_V):
        for j in range(1, MAX_V):
            if gcd(i, j) == 1:
                coprimes[i].append(j)

    results = []
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        arr = list(map(int, data[idx : idx + N]))
        idx += N
        
        last_seen = [-1] * MAX_V
        ans = []
        
        for i, val in enumerate(arr):
            max_idx = -1

            for cp in coprimes[val]:
                if last_seen[cp] > max_idx:
                    max_idx = last_seen[cp]
            
            ans.append(str(max_idx))
            last_seen[val] = i
            
        results.append(" ".join(ans))
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()
