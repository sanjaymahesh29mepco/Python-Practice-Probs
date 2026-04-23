import sys

def solve():
    MOD = 10**9 + 7
    
    try:
        line1 = sys.stdin.readline()
        if not line1: return
        n = int(line1.strip())
        line2 = sys.stdin.readline()
        if not line2: return
        a = list(map(int, line2.split()))
    except ValueError:
        return

    # even_sum tracks sum of dp[j] where prefix XOR parity is 0
    # odd_sum tracks sum of dp[j] where prefix XOR parity is 1
    even_sum = 1 
    odd_sum = 0
    current_prefix_xor = 0
    ans = 0

    for x in a:
        current_prefix_xor ^= x
        # Check parity of set bits in current prefix XOR
        # bin(n).count('1') % 2
        if bin(current_prefix_xor).count('1') % 2 == 1:
            # We need a previous prefix with even parity to make this subarray odd
            ans = even_sum
            odd_sum = (odd_sum + ans) % MOD
        else:
            # We need a previous prefix with odd parity to make this subarray odd
            ans = odd_sum
            even_sum = (even_sum + ans) % MOD
            
    print(ans % MOD)

line = sys.stdin.readline()
if line:
    t = int(line.strip())
    for _ in range(t):
        solve()
