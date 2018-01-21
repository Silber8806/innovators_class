prompt="""
Alright, let's do one last thing with imports.
We will discuss the concept of a package.
What is a package?

A package is just python files or modules living
within a directory and treated as a single unit.

If my main code lived on the top level:

	main.py
	useful_package/lesson_imports1.py
	useful_package/lesson_imports2.py
	__init__.py

Then the directory useful_package is 
a package, which contains 2 modules
or python files lesson_imports1.py
and lesson_imports2.py.

Packages aren't too complicated!

Why the "__init__".py file?  The __init__.py
file tells python that lesson_imports is 
a package.  It initializes it as a set
of modules!
"""

raw_input(prompt)

import useful_package

prompt="""
Let's look at the package first:
"""

raw_input(prompt)

help(useful_package)

import useful_package.lesson_imports
import useful_package.lesson_imports2

prompt="""
We can look at each modules too!
"""

raw_input(prompt)

help(useful_package.lesson_imports)
help(useful_package.lesson_imports2)


prompt="""
How about retrieving the functions to use!
"""

raw_input(prompt)

import useful_package.lesson_imports.useful_function as use_me
import useful_package as up
import up.lesson_imports2 as i2
from i2 import more_useful_function as add

use_me()
result = add(3,5)
print(result)


prompt="""
The same logic that applies to modules also applies to packages!
We just add more dots.  What's cool about packages is that

	lesson_imports
	lesson_imports2

could have the same function. We just use the lesson_imports and 
lesson_imports2 namespaces to access them.

If we have multiple packages.  We can even have similarly named
modules or functions.  The <package>.<library> combo will help
us distinguish between them.

What about if we wanted to extend our program to 2 directories 
deep.  It's possible to do this by just adding __init__.py
to a folder within the package.  This creates a sub-package.
We'd access the module within the subpackage as follows:

	<package>.<subpackage>.<module>.<lesson>

Obviously having many packages or modules can be rather tiresome
so I always recommend trying to stick with the lowest number of
modules and if you have to packages.  Always look for logical
ways to do this! 
"""

raw_input(prompt)

