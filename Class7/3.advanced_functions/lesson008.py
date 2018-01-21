prompt="""
We finally figured out how functions work on a
basic level.  We also figured out how to separate
out functions into different files and have them
all present in the "imported" function through 
the import statement.  We finally showed how you
could even separate python code into directories.

What is next?

Now is where we get into the most interesting aspects
of functions.  That is, they are objects in their own
right.  The implications will be explored in the next
few lessons.

This section of code is where it gets "weird".
"""

raw_input(prompt)

def i_am_called_sam():
	print("I am Sam wise!")
	return 0

print
print("This is a function reference!")
print(i_am_called_sam)

i_am_called_jane = i_am_called_sam

print
print("wait? did i_am_called_sam become i_am_called_jane?")
i_am_called_jane()

prompt="""
What happens when you take the name of a variable (after defining it)
and assign it to a variable.  The answer is?  The new variable points
to the function originally defined by <name>.  It is also
callable in the same way?  What makes a object like a function callable?
"""

raw_input(prompt)

def i_am_called_sam():
	print("I am Sam wise!")
	return 0

print("properties:")
for k in dir(i_am_called_sam):
	print(k)

print
print("the __call__ function within the function is what makes it callable!")
i_am_called_sam.__call__()

prompt="""
The thing is a function is just an object.  The def just associates a variable:

	<name> 

to it.  The function itself can be referenced by other variables.  In the above 
case, both i_am_called_sam and i_am_called_jane both point to the same variable.

Both of these variables can be called, because the __call__ method exists.
"""

raw_input(prompt)

def first_function():
	print("first")
	return 0

def second_function():
	print("second")
	return 0

def third_function():
	print("third")
	return 0

func_list = [first_function,second_function,third_function]
func_dict = {'first':first_function, 'second':second_function, 'third':third_function}

print
print("Yes, we just used a list of functions!")
for foo in func_list:
	print("*******")
	foo()
	print("*******")

print
print("Yes, we can even do it through a dictionaries")
for k,v in func_dict.iteritems():
	print("*******")
	print(k)
	v()
	print("*******")

prompt="""
An interesting property of mutable objects like lists and dictionaries
is that membership is just a reference to an object.  Those objects 
can be lists, dictionaries, primitives: strings/numbers and ....
suprisingly enough functions themselves.
"""

raw_input(prompt)

def i_r_a_function():
	print("pretty boring function!")
	return 0

def u_b_a_function():
	print("also pretty boring!")

def i_call_you_maybe(message,func):
	print(message)
	func()
	return 0

print
print("first function:")
i_call_you_maybe("message of the day!",i_r_a_function)

print
print("second function:")
i_call_you_maybe("second message of the day!",u_b_a_function)

prompt="""
Another interesting property of functions references is they 
can be passed into parameters as values and then called
generically in code.

In the above, func is any function passed in as a value.  It
will be called at func(). 

That means if I pass:

	i_call_you_maybe(<message>, i_r_a_function)

It will print the message and then call i_r_a_function.  On the 
other hand:

	i_call_you_maybe(<message>, u_b_a_function)

will print the message and then call u_b_a_function.

The function reference in the parameter determines what function gets
executed in the <code> body!
"""

raw_input(prompt)

def power_rules(number,power):
	return number ** power

def square(number):
	return power_rules(number,2)

def cube(number):
	return power_rules(number,3)

print("squares:")
square(5)

print("cubes!")
cube(5)

print
print("let's have fun!")
multiples = [(square(n),cube(n)) for n in range(25)]
for v,x in multiples:
	print(v,x)

prompt="""
We can also use a function call within a return statement.  The above 
functions, square and cube, are called partial functions.  They are 
partial, because the "full" function is defined elsewhere and the 
cube/square just provide a subset of the parameters.  They simplify
the calculation for people doing mostly squares and cubes.
"""

raw_input(prompt)



