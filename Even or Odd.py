list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
eve = 0
od = 0
for num in list:
    if num % 2 == 0:
        eve += 1
    else:
        od += 1
print("The even values are",eve)
print("The odd values are",od)