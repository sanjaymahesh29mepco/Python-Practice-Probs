def interchange_first_last(lst):
    if len(lst) < 2:
        return lst
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst
list = [11,22,33,44,55,66]
print("Original list:", list)
print("Modified list:", interchange_first_last(list))
