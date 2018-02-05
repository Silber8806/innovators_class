prompt="""
Let's begin our program properly.

A common practice amongst software engineers 
is the concept of a main function.

Main is the main entry point of code and represents
 the start of all execution.

We use a construct:

if __name__ == "__main__":

to have main run only when it is the script being 
called from the command line.

This allows use to import and re-use any functions
defined in this file without worrying about 
any logic being executed.  It is a nice feature, 
but not necessary for most scripts!
"""

raw_input(prompt)

def main():
	""" main entry point of program """ 
	print "this is a test program and entry point!!"
	return 0

if __name__ == "__main__":
	main()