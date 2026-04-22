import re

pattern = r"^(?!.*(\d)(-?\1){3})[456]\d{3}(-?\d{4}){3}$"

for _ in range(int(input())):
    s = input().strip()
    if re.match(pattern, s):
        print("Valid")
    else:
        print("Invalid")
