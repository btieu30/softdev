def middle_way(a, b):
    #we know the length is 3, so the middle of both arrays would be index
    # 1, so we create a new array with both vals at index 1 from a and b
    return [a[1], b[1]]

print(middle_way([1, 2, 3], [4, 5, 6])) # [2, 5]
print(middle_way([7, 7, 7], [3, 8, 0])) # [7, 8]
print(middle_way([5, 2, 9], [1, 4, 5])) # [2, 4]