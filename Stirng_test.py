a=input("enter the string: ")
if(a.isspace()):
    print("Conatins Space")
else:
    print("")
print("")
if(a.isalpha()):
    if("a","e","i","o","u" in a):
        print("Contains Vowels")
    else:
        print("Contains Consonants")
else:
    print("")
print("")        
if(a.isnumeric()):
    print("Contains Numbers")
else:
    print("")
print("")
if(a.isalnum()):
    print("")
else:
    print("Contains Special characters")
print("")