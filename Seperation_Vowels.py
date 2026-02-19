def move(s: str) -> str:
    vowels='aeiouAEIOU'
    s=list(s)
    l=0
    r=0
    while r<len(s):
        if s[r] not in vowels:
            s[l], s[r]=s[r],s[l]
            l+=1
        r+=1
    return ''.join(s)
print(move("Hello"))  
print(move("Computer"))