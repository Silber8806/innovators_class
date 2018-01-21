prompt="""
In previous lesson, we defined a function
and then showed how to use it with a 
function call.  

We defined a very simple function and 
left out two important features:return
statement and parameters.

In this lesson, we will cover the return
statement.  Before we cover it, we should
talk a bit about another topic!  The 
"call stack".

When you define a function, we bind a <name>
to some <code>,<parameter combo:
	
	<name> => (<code>,<parameters>)

The question is, what is a "function call"?

	<name>(<parameters>)

When Python sees a function call, it records
the location of the call within the file.
It does so by placing it ontop of the 
"call" stack.

	<name>(<parameters>) => call_stack[ line: 151 ]

It then executes the code, until it reaches a return
statement.  This means return control to the previous
location.  

When we defined a function in previous lesson, there
was no "return" statement at all.  So, the above statement
can't be true?  Well actually it is!  Python assumes
that any function without a return statement is actually
returning None:

	def hello_world():
		print("hello world")

the return statement is implied:

	def hello_world():
		print("hello world")
		return None

It's implied.  What happens when it reaches a return statement?
It looks in the call stack, removes the line reference and then
goes back to the line of code where the call occurred.  

What about the second parameter in return <object>.  Well
any python function can return another object or primitive.  This 
is used mustly for assignment. 

Let's do some exercises!
"""

raw_input(prompt)

def ira_function():
	print("Yes, I am!")

print(ira_function())

def ira_function_too():
	print("Yes, I am!")
	return None

print(ira_function_too())

prompt="""
Let's test the assumption that the return value is implied to be None 
if it is not defined.  We create 2 functions, one with a return None 
clause and another not.  We than print the function call to the screen.
"""

raw_input(prompt)

def foo():
	return 5

print(foo())
foo_fighters = foo()
print(foo_fighters)


def i_am_a_string():
	return "I am a string!"

print(i_am_a_string())
string_yes_i_am = i_am_a_string()
print(i_am_a_string())


prompt="""
If the return statement always returned None, there would be no point in
having it.  The question is, what is the use for it.  In the above, we
show that you can return many different values.  More importantly, 
we can assign the return value to a variable.
"""

def i_am_a_string():
	return "I am a string!"

print(i_am_a_string)

raw_input(prompt)

prompt="""
What if we left out the parenthesis?  What would happen?  It ends up giving us
just the function object itself.

	<function i_am_a_string at 0x1007258c0>

What is the strange "at 0x1007258c0" mean?  It's the reference in memory to the 
function itself.  This again confirms that to execute a function you have to 
call it.  the name of the function is actually a reference to the function 
definiton.
"""

raw_input(prompt)


i_am_a_doctor=1

def doctor():
	if (i_am_a_doctor == 1):
		doc = "doctor"
	else:
		doc = "not a doctor"
	return doc

is_doctor = doctor()
print(is_doctor)


prompt="""
By defintion, if the return value doesn't vary, it's usefulness is questionable.
Why not define a variable and be done with it?  The fact is, a function has a 
reference any variable defined outside of it.  In the above case, i_am_a_doctor 
is accessible.

We can therefore, use previously defined variables within the doctor function.
Note, the things within the function are not accessible outside of it!
"""

raw_input(prompt)

i_am_a_doctor=0

def doctor():
	if (i_am_a_doctor == 1):
		return "doctor"
	else:
		return "not a doctor"

is_doctor = doctor()
print(is_doctor)

prompt="""
Note that the doctor function can be converted to a function with 2 return statements.
The trick to remember is that the if statement has 2 conditional code blocks.  Only the
return statement that is executed results in the function exiting.
"""

raw_input(prompt)


def crazy_function():
	return 1
	print "this will never execute"
	while(True):
		print("never printed!")
	print("no worries about this either")
	return "a return that is never executed!"

crazy_function()

prompt="""
crazy_function contains a ton of code including a never ending loop!
Does it ever execute?  Once the function sees a return statement (first line),
no other code gets executed.  This is an important thing to note!
"""

raw_input(prompt)

hospital_list = ['mass general', 'beth israel', 'mt auburn']

def hospitals():

	a_dict = {}

	for l in hospital_list:
		a_dict[l] = []

	return a_dict

print(hospitals())
print(hospitals()['mass general'])

prompt="""
What can a function return?  A function can return most objects.  This includes
things like "lists", "dicts", primitives (integers, strings).  It can even return
objects and functions.  We will cover that later.  In the above, you can see
the function returns a dict from a list.

Notice that in the above case, <name>(<parameters) is actually a reference to the 
object being returned.
"""

raw_input(prompt)

prompt="""
Alright, so how is this any different from if statement except on a different line?
Why should I care about putting the code into a variable instead of just writing it 
down.  There has to be a point to all this code separation and execution!

The answer is, yes, definitely yes.  That's when we introduce (<parameters>).
"""

raw_input(prompt)



