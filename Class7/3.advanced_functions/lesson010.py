prompt="""
Alright, we showed how functions are objects and
can be used with variables.

We expanding on that by showing a list and dictionary
used to call all functions present!  This is common
if you want to register or deregister a set of functions
for data processing (if they don't apply to all situations).

The last thing we checked was partial functions.  Where
we "call" another function at the ending of a function 
with a subset of the parameters filled out!

This section gets even stranger?  We use a function
to define another function and then pass 
that function reference (not call) back?  

This strange concept is called a decorator!  It gets
at the essense of functions as objects!

This is best seen in examples!
"""

raw_input(prompt)

def upper_func():
	data = 'hello world!'
	def lower_func():
		print(data)
		return None
	return lower_func

new_func = upper_func()

print(new_func())

prompt="""
before we talk about decorators, let's look into the concept
of a closure:

	def upper_func():
		data = 'hello world!'
		def lower_func():
			print(data)
		return lower_func

	new_func = upper_func()

	print(new_func())

A function defined within another function is called a nested function.
A nested function can have a reference to the outer functions data 
(because it is being defined and not executed!).  

What exactly is data in this case?  Since it is being defined, the 
data in the upper function gets substituted fro the data 
in the lower_func().  The result is that upper_func variable is 
embedded in the lower_func().  When variables get embedded in
nested function it is called a closure.
"""

raw_input(prompt)

def login(func):
	def wrapper():
		print "you have successfully logged on!"
		func()
	return wrapper

def first_function():
	print "I am first!"
	return 0

def second_function():
	print "I am second!"
	return 0

print
print("function without decorator!")
first_function()
print
print("second function without decorator!")
second_function()

print
print("let's add a decorator?")
new_first_func = login(first_function)
new_second_func = login(second_function)

print
print("new first function?")
new_first_func()

print
print("new second function?")
new_second_func()

prompt="""
The first time I saw this type of code?  I was really confused?

I will explain this in small steps:

1. We define login with a func parameter (a function):

	def login(func):

The important thing to note is that the parameter is the name of 
a function called func!

2. A new nested function gets defined called wrapper!

	def wrapper()

Based on the first lesson, when we define a function, it associates
<name> with <code>.

	<name> => <code>

3. What is the <code> defined in wrapper?

	print "You have successfully logged on!"
	func()

the print statement is basic python language, but what about the function?
When we pass in a function at step 1.  It associates:

	func = (<value>)

that then gets substituted into the code.  This is the application of a closure.

	print "You have successfully logged on!"
	value()

4. the last statement is to return wrapper function.  Why?

No matter what <value> we pass in, the print statement is added 
to it and followed by the call: <value>().  This is a generic
way to add "you have successfully logged on" to any function!
"""

raw_input(prompt)

def login(func):
	def wrapper():
		print "you have successfully logged on!"
		func()
	return wrapper

def first_function():
	print "I am first!"
	return 0

def second_function():
	print "I am second!"
	return 0

print
print("function without decorator!")
first_function()
print
print("second function without decorator!")
second_function()

print
print("let's add a decorator?")
first_function = login(first_function)
second_function = login(second_function)

print
print("new first function?")
first_function()

print
print("new second function?")
second_function()

prompt="""
Let's modify the code a bit more.  We change
the variable name to the function being 
passed in.  

Since variables evaluate things on the right 
first, it provides us with the new "wrapper"
function.  So:

	login(first_function)

returns the wrapper and:

	first_function =

associates first_function with the wrapper.

We can now call first_function:

	first_function()

and it calls the new modified version of first function!

We do the same thing with second function!
"""

raw_input(prompt)


def login(func):
	def wrapper():
		print "you have successfully logged on!"
		func()
	return wrapper

@login
def first_function():
	print "I am first!"
	return 0

@login
def second_function():
	print "I am second!"
	return 0

print
print("new first function?")
first_function()

print
print("new second function?")
second_function()

prompt="""
Programmers got so lazy of typing the previous 
output, that they created a new symbol for:

	first_function = login(first_function)

This symbol is:

	@<decorator>
	def <name>(<parameters>)

This automatically applies the login function 
to the function definition.  It makes the code
a lot easier to read and is more process.

If I want to know what @login does, I just have
to look at login function and see what code 
is added to the wrapper.

I can also at a glance see where login applies
as the @ symbol quickly gives it away!
"""

raw_input(prompt)

def login(func):
	def wrapper(*args,**kwargs):
		func(*args,**kwargs)
	return wrapper

@login
def first_function(log_message):
	print "I am first!"
	return 0

@login
def second_function(log_message):
	print "I am second!"
	return 0

print
print("new first function?")
first_function("message!")

print
print("new second function?")
second_function("my message!")

prompt="""
We can modify the decorator so that 
it can decorate functions that have 
parameters.
"""

raw_input(prompt)


prompt="""
Note, some people can get very deep
on the subject of a decorator applying
decorators within decorators!  Often
complex decorators can create a lot of
complexity, which makes it hard to manage.

Decorators can be useful when you want to
modify a series of functions all at once
(decorating).
"""

raw_input(prompt)



