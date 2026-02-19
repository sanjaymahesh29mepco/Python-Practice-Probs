def pal(s):
    return s == s[::-1]
def sp(word):
    n = len(word)
    for i in range(1, n - 1):
        first = word[:i]
        if pal(first):
            for j in range(i + 1, n):
                second = word[i:j]
                if pal(second):
                    third = word[j:]
                    if pal(third) and third:
                        return first, second, third
    return "Impossible"
word = input("Enter the string: ")
result = sp(word)
if result == "Impossible":
    print(result)
else:
    print("Palindromic substrings:", result)