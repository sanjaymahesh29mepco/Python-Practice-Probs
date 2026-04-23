import sys

sys.setrecursionlimit(200000)

def solve():

    try:
        line1 = sys.stdin.readline().split()
        if not line1: return
        n, m = map(int, line1)
        
        powers = list(map(int, sys.stdin.readline().split()))
 
        adj = [[] for _ in range(n + 1)]
        edges = []
        for i in range(m):
            u, v = map(int, sys.stdin.readline().split())
            adj[u].append((v, i))
            adj[v].append((u, i))
            edges.append((u, v))
            
    except ValueError: return

    tin = [-1] * (n + 1)
    low = [-1] * (n + 1)
    timer = 0
    bridges_idx = []

    def dfs(v, p_idx=-1):
        nonlocal timer
        tin[v] = low[v] = timer
        timer += 1
        for to, idx in adj[v]:
            if idx == p_idx: continue
            if tin[to] != -1:
                low[v] = min(low[v], tin[to])
            else:
                dfs(to, idx)
                low[v] = min(low[v], low[to])
                if low[to] > tin[v]:
                    bridges_idx.append(idx)

    for i in range(1, n + 1):
        if tin[i] == -1:
            dfs(i)

    bridge_powers = sorted([powers[i] for i in bridges_idx], reverse=True)
    
    max_sam = sum(bridge_powers[0::2])
    min_sam = sum(bridge_powers[1::2])
    
    print(f"{max_sam} {min_sam}")

solve()
