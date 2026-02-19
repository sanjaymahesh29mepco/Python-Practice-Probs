def isprime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def consum(n):
    primes = [2]
    count = 0
    for i in range(3, n + 1, 2):
        if isprime(i):
            primes.append(i)
    
    ans = 0
    for i in range(len(primes)):
      sumprimes = 0
      for j in range(i,len(primes)):
        sumprimes+=primes[j]
        if sumprimes>n:
          break
        if isprime(sumprimes) and sumprimes<=n and primes[i]==2:
          ans+=1
    return ans
    

N = int(input())
print("no. of Prime no.s are",consum(N))