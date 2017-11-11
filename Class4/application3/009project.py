import sys
import os
from collections import Counter

print("""
	Let's do something more interesting.

	Let's assume that the files containing
	data are in the same folder.  Now,
	Let's assume they all end in the word
	data.

	We can do:

	os.listdir to get a name of files in a directory.

	we can than do:

	import os

	for file in os.listdir('.'):
		if (file.endswith(.data)):

	to pick only those files with .data in them and
	process them from that point on.

	In this specific example, we will ask the user
	if they want to process a file, if so,
	we will create a word count summary.  If not
	we will skip the file processing.

	""")

for file in os.listdir('.'):
	if (file.endswith('.data')):
		user_input = ''
		while(user_input != 'no' and user_input != 'yes'):
			user_input = raw_input("Do you want to process: %s yes/no?" % file)
			if (user_input != 'no' and user_input != 'yes'):
				print("ERROR: please provide valid input!!!")

		if (user_input == 'no'):
			continue

		in_file = open(file,'r')
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
		out_file = file.replace('.data','_summary.txt')
		raw_input("Let's write the top 100 words to a file for later use:")
		summary = open(out_file,'w')

		summary.write('%s Analysis:\n' % file)
		summary.write(str(word_counter.most_common(100)))
