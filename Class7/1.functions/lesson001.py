prompt="""
Per the lecture, functions are executable code blocks
or templates with one twist.  They have a function 
signature (<parameters>) that define a set of 
temporary variables used within the code.  They also
have return statements, which tell the program how
to exit out of the code block.  A function is always
first defined and then called.  Called is a fancy
way of saying executed.  Definitions below:

def <name>(<parameters>):
	<code>
	return <object>

def - keyword to "define" a function.  It associates

	<name> => (<parameters>,<code>) 

combination.

<parameters> - a list of temporary variable names and 
possible default values.  These are only defined within
the code itself and are "undefined" outside of it.

<code> - code block similar to an if, elif, else and 
or while block.  This code ends up executed during
a function call.

return <object> - return keyword marks the end of a 
code block procedure specific to functions.

An important thing to know about functions is that to
use the function you have to first define it as above
and then call it.  Calling is done below:

	<name>(<parameter values>)

This initiates the parameters by producing temporary variables
assigning the parameter values to it.  Then executing the code
block until it reaches a return statement.

The point in the file where the "call" occurs is where the code
returns to after the function finishes (hence the phrase return).

The object is used for variable assignment.

	<variable> = <name>(<parameter values>)

We will begin functions with the bare minimum requirements for a 
function and build up the complexity over the next few lessons.

"""

raw_input(prompt)

def hello_world():
	print("hello world!")

prompt="""
Let's begin with the most basic definition!  A 
function that binds the variable 

	hello_world

to a code block:
	
	print("hello world!")

defining a function does not cause anything to happen
instead it creates an object called a function tied 
to a variable.  To use a function we have to "call"
it.
"""

raw_input(prompt)

hello_world()

prompt="""
We do our first function call!  The program goes line-by-line
from top to bottom until it reaches the "def" keyword.  It then
creates the function bound to the <name>.  It then goes down
until it reaches the function call: hello_world().

Once it reaches the function, it loads the function into memory.
Since there are no parameters, it executes the code block!  The 
result is "hello world" being printed to the screen.  Once the 
function is done or gets to the bottom, it "returns" to the
function call and proceeds down the file!
"""

raw_input(prompt)

hello_world()
hello_world()
hello_world()

prompt="""
Function calls are independent.  They execute one at a time, 
top-to-bottom and always return to the line where the call
occurred.  In the above case, the function is called 3 times
and goes through the code 3 separate times.
"""

raw_input(prompt)

hello_world()
def hello_world():
	print("hello world back!")
hello_world()
hello_world()

prompt="""
Like variables, functions can be re-defined anywhere in the code.
When python sees "def" keyword it re-binds the variable:

	hello_world

with the new code block!  In this sense, define can be seen as 
similar to the assignment operator!
"""

def i_never_get_called():
	print("This should never show up!")

raw_input(prompt)

prompt="""
What if we define a function that we never use?  Than the code
never gets called and it goes to the bottom of the file.  Later
on we will see that this can be common for a file with 100s of
functions.  You might only end up using a few (while other people
using the file might use different functions.)
"""

raw_input(prompt)


