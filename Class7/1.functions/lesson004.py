prompt="""
An important, but more subtle aspect of code
is called scope.  

What is scope?  Scope applies to variables.
Scope is the section of <code> in which a 
variable can be accessed.  We typically 
talk about 2 types of scope:

1. Global Scope
2. Local Scope

Global scope is the easiest to understand.
It is any variable declared outside of a 
function or modified by the use of the 
global keyword.  By default, a global 
variable can be used anywhere in the code.

Local scope is a bit harder to understand.
When we declare a variable we put the line
of code on a call stack:

	<name>(<parameters>) => call_stack[line 151]

We also reserve a bit of extra memory for <parameters>
which accept the values we pass in them as well
as any variables defined within the <code> block.

You will find out that any variable declared within
a function is only accessible within the function.
If you try to access it outside the function, it 
will act like the variale does not exist!

Note, not all languages behave in this manner.  The
R programming language uses something called 
lexical scope.  Lexical scope starts at the scope 
where a variable is defined and then progressively
searches other functions and the larger context
for a specific variable reference.

Examples...note we will comment out the code
that produces "errors" to test this out
just comment it back in.
"""

raw_input(prompt)

this_is_global=5
print(globals()['this_is_global'])

prompt="""
We first define a variable within the file.
This is at global scope.  We can confirm this
by using:

	globals() 

Anything defined outside the function will be 
global to your script and can be accessed 
within functions defined after it.
"""

raw_input(prompt)

this_is_global=5

def local_variables():
	print("is this_is_global global scope?")
	print(globals().has_key('this_is_global'))
	print("is this_is_global local scope?")
	print(locals().has_key('this_is_global'))
	print(this_is_global)
	return None

local_variables()

prompt="""
We can confirm global scope of this_is_global
by defining it outside the function and 
using it inside the function.  Note 
that it isn't in the local() list.

This makes sense, local only applies to within
the function.  Once outside the function it 
should no longer apply.  Global scope 
applies to any seciton of the code.
"""

raw_input(prompt)

def local_parameters(this_is_a_param):
	print("is this_is_a_param global scope?")
	print(globals().has_key('this_is_a_param'))
	print("is this_is_a_param local scope?")
	print(locals().has_key('this_is_a_param'))
	return None

local_parameters('silly')	

#print(this_is_a_param)

prompt="""
Let's now test the <parameters>.  You can see
that in this specific case they have local scope.
You can't use the this_is_a_param outside of
the function.  It can only be used in the 
<code> block.
"""

raw_input(prompt)

def local_variables():
	this_is_local=5
	print("is this_is_local global scope?")
	print(globals().has_key('this_is_local'))
	print("is this_is_local local scope?")
	print(locals().has_key('this_is_local'))
	return None

local_variables()

#print(this_is_local)

prompt="""
The local scope also applies to variable defined
within the code block, but not outside of it.
This means that we have to be careful not 
to define values in the function that we 
later want to access outside of it.
"""

raw_input(prompt)

this_was_local=5

def global_modifier():
	this_was_local=3
	print("is this_was_local global scope?")
	print(globals().has_key('this_was_local'))
	print("is this_was_local local scope?")
	print(locals().has_key('this_was_local'))
	return None

global_modifier()

print(this_was_local)

def global_modifier():
	global this_was_local
	this_was_local=500
	print("is this_was_local global scope?")
	print(globals().has_key('this_was_local'))
	print("is this_was_local local scope?")
	print(locals().has_key('this_was_local'))
	return None

global_modifier()

print(this_was_local)

prompt="""
Let's say that we really wanted a variable 
to link back to a varaible defined in the 
global context.  To accomplish this, we 
can use the "global" keyword in front 
of a variable name.

In the above example, this_was_local had
both a global() and local() presence.  That
means that there is a different context for
the two variables based on the code it is embedded
in.  If you change the value outside the function
it only applies outside the function.  If you
change the value within the function, it only 
applies to that specific <code> block.

To force the function to reference the global context
we use the "global" keyword in front of it.
This causes the reference to the local variable 
to dissapear.  The variable now references the 
global variable (which can be accessed anywhere).
"""

raw_input(prompt)

global_variable=True

def inner():
	inner_variable=True

	print("global variable:")
	print(global_variable)
	print("outer variable:")
	try:
		print(outer_variable)
	except:
		print("False")
	print("inner variable:")
	print(inner_variable)

	print("inner locals")
	print(locals())

def outer():
	outer_variable=True

	print("enter outer function!")
	print("global variable:")
	print(global_variable)
	print("outer variable:")
	print(outer_variable)
	print("inner variable:")
	try:
		print(inner_variable)
	except:
		print("False")

	print("outer locals:")
	print(locals())

	print("enter inner function")
	inner()
	print("exit inner function")

	print("outer locals:")
	print(locals())

	print("global variable:")
	print(global_variable)
	print("outer variable:")
	print(outer_variable)
	print("inner variable:")
	try:
		print(inner_variable)
	except:
		print("False")

	return 0


print("leaving global space")

outer()

print("entering global space")

print("global variable:")
print(global_variable)
print("outer variable:")
try:
	print(outer_variable)
except:
	print("False")
print("inner variable:")
try:
	print(inner_variable)
except:
	print("False")

prompt="""
We can see in the above exercise, that
python local scope applies only to the 
function it is declared in.  It is scoped
to it's <code> block.

Even though inner is called, it can't access
the variables within outer function.  The 
same applies to outer function, it can't access
anything defined within the inner function.
Global variables, however, are accessible in 
both inner and outer functions.

Note:

	try:
		print(<variable>)
	except:
		print("False")

return False only when python can't find <variable>
in the code.  You would get a global <variable> 
is undefined otherwise.
"""

raw_input(prompt)

