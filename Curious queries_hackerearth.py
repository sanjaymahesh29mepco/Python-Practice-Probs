import sys

def solve():
    # Fast I/O
    input = sys.stdin.read().split()
    if not input: return
    idx = 0
    
    T_cases = int(input[idx])
    idx += 1
    
    for _ in range(T_cases):
        N = int(input[idx])
        Q = int(input[idx+1])
        idx += 2
        
        A = [int(x) for x in input[idx : idx + N]]
        idx += N
        
        queries = []
        for i in range(Q):
            L = int(input[idx])
            R = int(input[idx+1])
            queries.append((L, R, i))
            idx += 2
            
        # Coordinate Compression
        sorted_vals = sorted(list(set(A)))
        rank_map = {val: i + 1 for i, val in enumerate(sorted_vals)}
        M = len(sorted_vals)
        
        # Group queries by L
        queries_at = [[] for _ in range(N)]
        for L, R, q_idx in queries:
            queries_at[L].append((R, q_idx))
            
        bit = [0] * (M + 1)
        def update(i, delta):
            while i <= M:
                bit[i] += delta
                i += i & (-i)
        
        def query_bit(i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & (-i)
            return s
            
        results = [0] * Q
        current_sum = 0
        
        for i in range(N):
            val = A[i]
            update(rank_map[val], val)
            current_sum += val
            
            for R, q_idx in queries_at[i]:
                # sum of A[j] > A[R] is total_sum - sum of A[j] <= A[R]
                target_val = A[R]
                rank_R = rank_map[target_val]
                less_equal_sum = query_bit(rank_R)
                results[q_idx] = current_sum - less_equal_sum
        
        print(*(results))

solve()
