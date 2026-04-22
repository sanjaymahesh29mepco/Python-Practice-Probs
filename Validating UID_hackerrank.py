import re

def validate_uid(uid):

    if len(uid) != 10:
        return "Invalid"
    
    if not uid.isalnum():
        return "Invalid"
    
    if len(set(uid)) != 10:
        return "Invalid"
    upper_count = sum(1 for char in uid if char.isupper())
    if upper_count < 2:
        return "Invalid"
    
    digit_count = sum(1 for char in uid if char.isdigit())
    if digit_count < 3:
        return "Invalid"
    
    return "Valid"

try:
    t = int(input().strip())
    for _ in range(t):
        uid = input().strip()
        print(validate_uid(uid))
except EOFError:
    pass
