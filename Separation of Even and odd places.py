a=input("Enter the string!!!")
l1=[]
l2=[]
for i in range (0,len(a)):
    if i%2==0:
        l1.append(a[i])
    elif i%2!=0:
        l2.append(a[i])
print(l1)
print(l2[::-1])
