from sys import argv

script, input_file = argv

def rewind(f):
    f.seek(0)

def print_current_line(f):
    print f.readline()

def print_all(f):
    print f.read()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like tape"

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_current_line(current_line, current_file)

current_line += 1
print_current_line(current_line, current_file)

# There is no ++ in Python
current_line += 1 
print_current_line(current_line, current_file)