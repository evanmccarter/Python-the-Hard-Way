def fill(numbers, max):
    i = 0
    
    # while i < range:
    while i in range(0, max):
        print "At the top i is %d" % i
        numbers.append(i)
    
        i = i + 1
        print "Numbers now ", numbers
        print "At the bottom i is %d" % i
    
    return numbers

    
nums = []
fill(nums, 2)
print "The numbers: "
for n in nums:
    print n