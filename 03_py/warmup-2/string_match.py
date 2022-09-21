def string_match(a, b):
    count = 0

    #find the string with the shorter length
    if len(a) < len(b):
        shorter = a
        longer = b
    else:
        shorter = b
        longer = a
    
    #loop through the shorter string, check every two chars to check for matches
    for x in range(len(shorter) - 1):
        if shorter[x] == longer[x] and shorter[x+1] == longer[x+1]:
            count = count + 1

    #return the overall count
    return count

    print string_match('xxcaazz', 'xxbaaz')
    print string_match('abc', 'abc')
    print string_match('abc', 'axc')