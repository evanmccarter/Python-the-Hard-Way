print "\\" 	# backslash
print "\'" 	# single quote
print "\""	# double quote
print "\a"	# ASCII bell
print "\b"	# backspace
print "\f"	# formfeed
print "\n"	# linefeed
print "\r" 	# carrige return
print "\t"	# tab


# carrige return and then append, overrides line 
print "hi there\r",
print "bye there"

while True:
	for i in ["/", "-", "|", "\\", "|"]:
		print "%s\r" % i,