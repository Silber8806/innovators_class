""" 
	Hello Innovators,

	I am talking to you through the help documentation.
	That documentation is defined through triple 
	quoted strings within each module (file) or 
	function.  

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



def main():
	"""
	This code is intended to be executed within the __name__
	section only.  It should never be used in imported files
	"""
	print("this is the main function within lesson_imports")
	return 0

if __name__ == 'main':
	main()