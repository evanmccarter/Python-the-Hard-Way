hairs = ['brown', 'blond', 'red']
eyes = ['brown', 'blue', 'green']
weights = [1, 2, 3, 4]

the_count = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for loop goes through a list
for number in the_count:
    print "This is count %d" % number

for fruit in fruits:
    print "A fruit of type: %s" % fruit

# also we can got hrough mixed listd too
for i in change:
    print "I got %r" % i

# we can also build lists
elements = []

for i in range(0,6):
    print "adding %d to list" % i
    elements.append(i)

# or elements = range(0,6)

for i in elements:
    print "Element was: %d" % i
    
