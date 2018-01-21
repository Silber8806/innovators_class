prompt="""
We talked about the utility of functions.
The most important aspect of functions 
and later objects is their social nature.
I don't mean you take functions to a 
dinner function.

Python has a huge developer community.  Those 
developers all want to save time and contribute
back to the community.  These developers
write files called <libraries>, which can be
used by other developers to save time.

The clever bit is how do you get code to other 
developers.  Python has something called the 
PyPI - Python Package Index:

	https://pypi.python.org/packages

It's accessible using two command-line tools 
(not within python, but on your terminal/commandline).

These are:

	easy_install <library>

which tends to not be used.  It's supposed to be deprecated.

	pip install <library>

which is the current standard (but I use easy_install on failure).

These commands will login to PyPI index and search for a <library>
and then download it to your global python instance.  It does not
install it in your local directory, because you might want to use
the <library> for multiple projects.  We will discuss, an important
problem with libraries later. specifically, when you are running
multiple version.

The question now?  What is a library.  We will develop a library
local to a specific project and then explain in detail how it 
differs from a library installed using pip.  You'll be surprised
to find it is quiet similar.

The first step in understanding libraries is to talk about the concept
of a module.  Imagine you have a Python program you wrote.  It becomes
several thousand lines long.  Some parts of your code, specifically functions
could be used in other scripts or programs you write.  A good example would be making an 
internet connection.  A way to handle this is to separate the functions 
that are reusable from the logic that is specific to the program (or business).
The reusable code could be isolated and separated into another file.  

You would then have two files in your directory.

	main.py # main python file
	lib.py # the re-usable functions

The question now is, how do we make sure main.py has access to all the cool
functions within lib.py.  The answer is the import statement:

	import lib

This executes the entire lib script, which is typically just a bunch of 
function definitions.  def statements.

Let's check this out within this folder.  We have two files, this file:

	lesson006.py

and a file to import:

	lesson_imports.py

Let's try some examples:
"""

raw_input(prompt)

prompt="""
Press enter to get "help" for the 
lesson_imports library.
"""

raw_input(prompt)

import lesson_imports

help(lesson_imports)

prompt="""
Open up the lesson_imports file and 
look at the contents.  Notice the 
triple quoted strings.

That is called a DOCSTRING and represents
the help documentation of a function or 
module.  

If you ever have reusable code, this 
feature of Python is super useful!

let's see how to use the code:
"""

raw_input(prompt)

import lesson_imports

lesson_imports.useful_function()
sum_of_it = lesson_imports.more_useful_function(3,5)
print(sum_of_it)

prompt="""
Noticed something odd about the imported functions!
They have a prefix?  All of the functions have a 
prefix:

	lesson_imports.<function>

Why?

What if you were importing many files.  Not just the
lesson_imports.  You might have many different 
functions called useful_functions (joke?).  

The <lesson_imports> is called the namespace of a 
function.  It makes sure that two different 
modules (files) can define the same function
without one overwriting the other!

Great, makes perfect sense.  Isn't all this rather
annoying.  Like maybe I'm only using one module
or maybe I don't want to type the namespace 
1000 times!
"""

raw_input(prompt)

from lesson_imports import useful_function

print
print "single import!"
useful_function()

from lesson_imports import useful_function, more_useful_function

print
print "many imports!"
useful_function()
more_useful_function(5,10)

print
print "rename useful_function to tasty_food"
from lesson_imports import useful_function as tasty_food

tasty_food()

print
print "rename the namespace as I hate the other guys naming convention"
import lesson_imports as lesson 

lesson.useful_function()

prompt="""
In the above section, we use 4 different import statements.
The first one imports a single function into this files 
global namespace as useful_function.

The second case imports two different functions.  You can
keep all imports on a single line.

The next case renames the import to tasty_food.  Now we
have a more accurate name of the function.  If lots of 
people are using "useful_function" or you don't like 
the naming convention or you want to replace one 
function in a <library> with another <library> without
changing it's name within the script, than this is 
an option.

What about if you don't like the <namespace> or module name,
you can change that with the fourth option.

Generally, with highly available libraries, it is best not 
to use to many as terms.  Developers that use them regularly
might not know about your specific conventions and will 
get confused.
"""

raw_input(prompt)


