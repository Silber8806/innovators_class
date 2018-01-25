prompt="""
A topic worth covering is the concept of anonymous
functions called lambda functions in Python.  Lambda's
origin comes from the paradigm called functional 
programming.  The 3 paradigms are:

	procedural
	functional
	object-oriented

Originally, Guido was not a fan of the lambda implementation,
but it's now an accepted part of Python.  lambda's work and 
act similar to JavaScript: reducers, mappers and functions in 
general.

What is a lambda?  Lambda is a function without a name:

	lambda x: x

is the same as:

	def no_name(x):
		print(x)

Why use this notation?  It's easier to read:

	lambda x: 2x

implies:

	x => 2x

It looks like, an input x maps to a process of twice
the value.

lambda's are used in python when a function needs to 
be provided, but it would be a pain to define one 
earlier on.  It's just easier to have a one use function!

"""

raw_input(prompt)

f = lambda x, y, z : x + y + z
print(f(1,2,3))

prompt="""
Above we show a lambda that adds 3 variables
and returns the value.  Pretty simple.
"""

raw_input(prompt)

multi_table = map(lambda x: (x,x ** 2),range(101))

for row in multi_table:
	print row

prompt="""
In the above case, we use a lambda function within 
a special function called map.  Map takes a function
(lambda) and applies it to an iterable object.  I 
decided to simplify it by using the range() generator,
which generates the sequence (0,1,2,3,4...100). 

You could substitute a list here and it would apply
the lambda over hte list.
"""

raw_input(prompt)

filtered_table = filter(lambda x: x % 2, range(101))

print("filter:")
for row in filtered_table:
	print(row)

filtered_multi_table = map(lambda x : (x, x ** 2), filtered_table)

print
print("multi_table applied to filtered_table:")
for row in filtered_multi_table:
	print(row)

prompt="""
map is one of 3 operations that can be used against an iterable class.
The other two are filter and reduce (similar to javascript equivalents).
filter takes a function that returns a boolean value (True/False) based
on the some input.  It then applies the function to all elements in
the iterable object.  If an object caused the function to return True,
it is added to a new list.  After the entire filter process is complete
it returns the new list of objects (only those that return True).
"""

raw_input(prompt)

reducer = reduce(lambda x, y: x ** 2 + y, range(5))
print(reducer)


prompts="""
reducer is the strangest of the 3 methods: map, filter and reduce.
A reducer starts with the first two indexes within an interable
object.  It applies them to the function pairwise.  The reducer
then takes the result returned by this operation and assigns it 
to the first argument of the function and then takes the "next" 
object from the iterable object.

It keeps reassigning the return to the first argument and all subsequent
arguments are retrieved from the iterable object until it is exhaused.

The final return for the reducer is the return of the last function call.

example:

	reduce(lambda x, y: x ** 2 + y, range(5))

	range(5) => (0,1,2,3,4)

	first_reducer => 0 ** 2 + 1 => 1
	second_reducer => 1 ** 2 + 2 => 3
	third_reducer => 3 ** 2 + 3 => 12
	fourth_reducer => 12 ** 2 + 4 => 148

	returns 148

Notice how the first_reducer takes the first 2 arguments within 
range.  Afterwards, the first object is the return of the previous
function and the second argument is the next element in the list.
"""

raw_input(prompt)
