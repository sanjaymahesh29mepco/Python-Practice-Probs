import sys

def solve():
    # Efficiently read all input at once
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    T = int(input_data[ptr])
    ptr += 1
    
    for _ in range(T):
        N = int(input_data[ptr])
        ptr += 1
        A = list(map(int, input_data[ptr : ptr + N]))
        ptr += N
        Q = int(input_data[ptr])
        ptr += 1
        
        # Parse and store queries with original indices
        queries = []
        for i in range(Q):
            L = int(input_data[ptr]) - 1
            R = int(input_data[ptr + 1]) - 1
            X = int(input_data[ptr + 2])
            Y = int(input_data[ptr + 3])
            ptr += 4
            queries.append((L, R, X, Y, i))
            
        # Mo's Algorithm Setup
        block_size = int(N**0.5) + 1
        # Sort queries: by block of L, then by R (with snake-like optimization)
        queries.sort(key=lambda q: (q[0] // block_size, q[1] if (q[0] // block_size) % 2 == 0 else -q[1]))
        
        freq = {}  # Stores frequency of each element in current range
        B = [0] * (N + 1) # B[i] = Bitwise XOR of numbers occurring exactly i times
        
        # Sqrt Decomposition on B to answer Range Sum Queries in O(sqrt(N))
        b_block_sz = int((N + 1)**0.5) + 1
        b_block_sums = [0] * ((N + 1) // b_block_sz + 1)
        
        def update_B(idx, val_xor):
            if idx == 0: return
            prev_val = B[idx]
            B[idx] ^= val_xor
            b_block_sums[idx // b_block_sz] += (B[idx] - prev_val)

        def add(val):
            f = freq.get(val, 0)
            if f > 0: update_B(f, val) # Remove from old frequency XOR sum
            f += 1
            freq[val] = f
            update_B(f, val) # Add to new frequency XOR sum

        def remove(val):
            f = freq[val]
            update_B(f, val) # Remove from current frequency XOR sum
            f -= 1
            freq[val] = f
            if f > 0: update_B(f, val) # Add to new frequency XOR sum

        def query_sum(X, Y):
            X = max(1, X)
            Y = min(N, Y)
            if X > Y: return 0
            
            res = 0
            start_blk = X // b_block_sz
            end_blk = Y // b_block_sz
            
            if start_blk == end_blk:
                for i in range(X, Y + 1):
                    res += B[i]
            else:
                for i in range(X, (start_blk + 1) * b_block_sz):
                    res += B[i]
                for i in range(start_blk + 1, end_blk):
                    res += b_block_sums[i]
                for i in range(end_blk * b_block_sz, Y + 1):
                    res += B[i]
            return res

        results = [0] * Q
        curL, curR = 0, -1
        
        # Process queries in Mo's order
        for L, R, X, Y, idx in queries:
            while curR < R:
                curR += 1
                add(A[curR])
            while curL > L:
                curL -= 1
                add(A[curL])
            while curR > R:
                remove(A[curR])
                curR -= 1
            while curL < L:
                remove(A[curL])
                curL += 1
            
            results[idx] = query_sum(X, Y)
        
        # Print results for current test case
        sys.stdout.write("\n".join(map(str, results)) + "\n")

if __name__ == "__main__":
    solve()
