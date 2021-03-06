""" 
	Hello Innovators,

	I am talking to you through the help documentation.
	That documentation is defined through triple 
	quoted strings within each module (file) or 
	function.  

	This is how we create the "help" documentation.

	Try the following:

		help(lesson_imports.useful_function)

	You will see it isolate the help advice to a 
	single function.

	To get out of this, use the following 2 keys:

	:q
"""

def useful_function():
	""" 
	A useless function that is pretending to be useful.

	call it to get good advice for today.
	"""
	print("You should eat tasty food today!")
	return 0

def more_useful_function(a,b):
	""" 
	A function that is actually useful, but only in the 
	most marginal sense.  It might even be considered
	annoying in terms of keystrokes.

	more_useful_function(a,b)

	returns the sum of a and b
	"""
	return a + b

def main():
	"""
	This code is intended to be executed within the __name__
	section only.  It should never be used in imported files
	"""
	print("this is the main function within lesson_imports")
	return 0

if __name__ == 'main':
	main()