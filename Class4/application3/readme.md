# We will open up a text and read it.

## Exercise 1, open up Kafka.data and read the entire file, print to screen:

http://www.gutenberg.org/cache/epub/5200/pg5200.txt

You will notice it is the full text of a famous work by Kafka.

The first exercise just opens the file and prints the contents to the screen.

You open files with:

open(<filename>,'r')

then use the read command on it:

open(<filename>,'r').read()

that gets all the contents as a string.

## Exercise 2, replace ' the ' with " <name>'s ". 

Open the kafka.data file, read it, replace ' the ' with " <yourname>'s > ".
print the content to the screen.

the file command is:

	str.replace(<pattern>,<replacement>)

## Exercise 3, lower case

Open the kafka.data file, read it, convert it all to lower case and then
do the previous replacement.  We were missing " The " and " THE " replacements
due to the capital letters. computers are picky!

## Exercise 4, count lines with " the "

Open the file and read it line-by-line.  Figure out the lines with " the " in it.
Count those lines.  Count the total number of lines as well.  What percent of lines
have " the " in them.

Use the:

<str>.find(<pattern>)

command to find out if the line contains " the ".  find returns -1 if no match is found
otherwise it returns the character number where " the " was found.

## Exercise 5, Counts

Use a few new functions to get word count of the file.

	<str>.split(' ') command converts a string into words.

You can then use:

	Counter(<str>.split(' ')) 

to get an object that maintains counts in descending order.

print the Counter afterwards to see the entire counts.  You can do:

	Counter(<str>.split(' ')).most_common(<number>) 

where number is the top <number> of counts present in the series.

## Exercise 6, Combine 3 files.

Combine Kafka, frankenstein and alice files into a single string.  Then
do the entire word analysis with this combined file.

## Exercise 7, learn how to write a file.

We can write to a file by opening it to write mode:

	open(<filename>,'w')

You can write to the file with:

	file_object.write(<string>)

## Exercise 8, make it more usable with the commandline.

We use the sys library to get the arguments from the commandline.

We can do:

	import sys

to load the system library code.

We can then get arguments from the commandline using:

	sys.argv[<number>]

where 0 is the name of the script being executed, 1 is the first arguemnt...2 second...n the nth.

	len(sys.argv)

That's the number of arguments minus 1.

This let's us do the following in the commandline:

	python 8project.py kafka.data

to process the kafka.data file.  If you change the name to alice.data, it will process for 
the alice.data file.

## Exercise 9, going through files in a directory.

We use the os or operating systems library to look through and pick only those files with
.data at end.  We then give a prompt for the user asking if they want to process the file.
Afterwards, we write the results to summary files.

We start with:

	import os

We then can do:

	for file in os.listdir('.'):
		if(file.endswith('.data')):
			...

where ... is your processing.  For my example, I use a raw_input to get a yes/no answer.
I do a while loop until I get a yes or no answer, then process it similar to the 
Count script in Exercise 5.

## 10, commandline processing

You don't have to do any of this work in python.  You can do a lot of it from the commandline.

We explore 3 commands that you can type in the commandline:

cat - prints out the contents of a file to screen.
wc - wordcount program.  You can provide it 3 options: -c, -w and -l for character, word and line counts.
grep - does a find command over each line and returns those lines that have a match.

In Bash, you can feed cat to wc using a pipe |.

cat <filename> | wc -l

will print all the lines of filename and forward them to the wc program, which does a line count.

The same can be done with grep and even the output of a python program.




