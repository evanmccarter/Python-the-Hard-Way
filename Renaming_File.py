from sys import argv
from os import remove

script, old_name, new_name = argv
reader = open(old_name, 'r')
data = reader.read()

writer = open(new_name, 'w')
writer.write(data)

reader.close()
writer.close()

remove(old_name)