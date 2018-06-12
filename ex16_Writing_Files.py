from sys import argv

# close - closes the file
# read - reads content of file
# readline - reads just one line of a file
# truncate - empties file
# write(stuff) - writes to file

# can read then write with same obj
# cannot write then read with same object

script, filename = argv

print "We are going to erase %r." % filename
print "If you dont want that, hit CTRL-C"
print "Else hit enter"

raw_input("?")

# r		reading
# w		writing
# a		appending

# r+	reading and writing
# a+	reading and appending

print "Opening the file..."
target = open(filename, 'r+')

print target.read()

print "Truncating the file. Good bye!"
target.truncate()

print "Now I'm going to asks you for 3 lines"

line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

target.close()

print "And finally, we close it"
target.close()