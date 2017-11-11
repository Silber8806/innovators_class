
print("""
	Let's go through the file line by line
	we can use the command:
	for line in kafka_file:
		<conditional code>

	to process each line separately.

	We can use the find command to 
	check each line for a word.

	strip, gets rid of the enter key \n 
	present in a single string.
	""")

kafka_file = open('kafka.data','r')

raw_input("We will go through each line looking for ' the ':")

i = 0
count = 0
lines = 0
for line in kafka_file:
	line = line.lower().strip('\n')
	found = line.find(' the ')
	i += 1
	if (found > -1):
		count += 1
	print
	print("TEST")
	print(line)
	print("found 'the': %s" % found)
	lines += 1

percent_lines = round((100 * (count / float(lines))),2)

print
print("We did our searches now!")
print("We have %s lines with ' the ' in it!" % count)
print("We have %s total lines..." % lines)
print("The percent with ' the ' is: %s" % percent_lines)
print("***This doesn't count sentences that start with the")