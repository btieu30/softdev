def common_end(a, b):
    #compare the beginning of both arrays (index 0) and
    # their ends (length of the array - 1, because indexing begins @ 0
    if a[0] == b[0] or a[len(a)-1] == b[len(b)-1]:
        return True
    return False

print(common_end([1, 2, 3], [7, 3])) # True
print(common_end([1, 2, 3], [7, 3, 2])) # False
print(common_end([1, 2, 3], [1, 3])) # True