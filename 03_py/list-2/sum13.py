def sum13(nums):
    sumu = 0
    #boolean to help determine whether or not we count the num at index x
    sta = False
    
    for x in nums:
        #if the num is unlucky 13, set sta to true
        if x == 13:
            sta = True
            continue #"continue" keyword ends current iteration, so we move to the num after 13
        if sta == True:
            #the num right after 13 is also unlucky, so we continue again, moving to the next num
            continue
        sumu += x #the num will be added to the grand sum
        
    return sumu

print (sum13([1, 2, 2, 1])) # 6
print (sum13([1, 1])) # 2
print (sum13([1, 2, 2, 1, 13])) # 6
