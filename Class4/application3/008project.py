import sys
from collections import Counter

print("""
	We will now generalize the previous script.
	We will create a script that accepts one argument on
	the command line.  If none is provided, it should
	exit without doing anything.  If it has an 
	argument, it should try to read the file and
	return a summary with a similar name.

	python 8project.py alice.data

	should create a file:

	alice_summary.txt

	To do this, you need to write:

		import sys

	You can then find out how many arguments there are
	using len(sys.argv).  If length is less than 2, you
	will want to exit using the sys.exit(1) command.  If
	there is 2 or more, take the second argument using:

		file_name = sys.argv[1]

	You can then use the file name from the commandline!

	""")

arguments = sys.argv

if (len(arguments) < 2):
	print("""

	*** ERROR ***

	USAGE: python 8project.py <filename> [optional]

	Takes filename, does a word count and write it 
	to a summary file for future consumption!
		
	*** ERROR ***

		""")
	sys.exit(1)

file_name = arguments[1]
in_file = open(file_name,'r')
contents = in_file.read().lower().replace('\n','')

print
raw_input("Check the contents, press any key!")
print(contents)

words = contents.split(' ')

print
raw_input("Create the words, press any key!")
print(words)

word_counter = Counter(words)
print
raw_input("Print the words counter:")
print(word_counter)

print
raw_input("The 10 top most common words:")
print(word_counter.most_common(10))

print
out_file = file_name.replace('.data','_summary.txt')
raw_input("Let's write the top 100 words to a file for later use:")
summary = open(out_file,'w')

summary.write('%s Analysis:\n' % file_name)
summary.write(str(word_counter.most_common(100)))
