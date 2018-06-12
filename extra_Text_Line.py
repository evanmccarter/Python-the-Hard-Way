

file_name = raw_input("Enter filename: ")
line_num = int(raw_input("Enter line you which to see: "))

opener = open(file_name)
opener.seek(line_num)
print opener.readline()