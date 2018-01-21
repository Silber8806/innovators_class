prompt="""
The last lesson dealt with function references
and showed how you could use a function 
to produce a slightly modified version of a 
function that was passed in.

We call this a decorator, because it's 
decorating or adding small bits of code 
to other functions.  

The next topic we cover and the last one!
Is the concept of "recursion".  What is 
recursion?  Recursion is when we define
a function, which calls itself!  

Note: recursive functions are like while 
loops, they can go on forever.  Python
will actually "kill" your code if this
happens.  
"""

raw_input(prompt)

def special_power_formula(number):
	if (number <= 0):
		return 0
	else:
		return number ** number + special_power_formula(number -1)

print("can you figure out the special power formula?")
for r in range(1,10):
	print
	print("special_power_formula(%s)" % str(r))
	print(special_power_formula(r))

prompt="""
In the above case, we do the following:

We take a number let's call it n and calculate:

	sum = (n ** n) + ((n - 1) ** (n - 1)) + ((n - 2) ** (n - 2))

for all values of n > 0.  If it's 0, we just add 0 to the above sum!

This might seem confusing, so I will quickly explain what is happening!

1. When we call special_power_formula with a number.
2. If number is less or equal to 0, it returns 0.  No other calculations happen.
3. If number is greater than 0. It skips to:

	return number ** number + special_power_formula(number - 1)

The first step is: 

	number ** number 

Easy to calculate with the parameter.  What about the second part:

	special_power_formula(number - 1)

It's the function itself?  Remember the call stack in lesson001?  When
a function call occurs, it adds it to the call stack:

	special_power_formula(number) => call_stack[ line 32 ]

It then initializes the function parameters and executes the code.  When it 
sees:

	special_power_formula(n - 1)

It adds an aditional line number to the call stack:

	special_power_formula(number) => call_stack[line 32, line 28]

It starts a "new" version of special_power_formula and executes the code.
Each time, the computer is keeping track of where the code has to return and
which "version" of the code is running.

It continues this process of special_power_formula calls until:

	if (number <= 0):
		return 0

The result is that special_power_formula(0) is returned to special_power_formula(1) at:

	return number ** number + special_power_formula(number -1)

That is:
	
	return 1 ** 1 + 0

How does it know where to return too.  It removes the last entry off the "call stack".

It returns to the next level function (special_power_formula(2)):

	return 2 ** 2 + 1

where 1 is the result of special_power_formula(1)

This returns to the next level function (special_power_formula(3)):

	return 3 ** 3 + 5

where 5 is the result of special_power_formula(2).

Each step, the function looks up the call stack, returns the value and continues the return
process.  That is, until the call_stack is exhausted and we reach the original number provided!

Let's see the example with special_power_formula(4) as a series of steps:



	first step: Add to call stack

	1. special_power_formula(4) is called.
	2. we add special_power_formula(4) to call stack (refernece to main code)

	3. special_power_formula(3) is called.
	4. we add special_power_formula(3) to call stack.

	5. special_power_formula(2) is called.
	6. we add special_power_formula(2) to call stack.

	7. special_power_formula(1) is called.
	8. we add special_power_formula(1) to call stack.

	9. special_power_formula(0) is called.
	10. we add special_power_formula(0) to call stack.




	second step: create an exit condition.  Prevents infinite calls.

	11. number <= 0, so 0 is returned. special_power_formula(0) = 0



	last step: remove from the call stack and return each value.

	12. we remove special_power_formula(0) from the call stack.
	13. we return to code: special_power_formula(1) the next value in the call_stack.
	14. we return to the return statement: n ** n + special_power_formula(n - 1)
	15. we substitute values: n = 1, special_power_formula(0) = 0.
	16. 1 ** 1 + 0 = 1, special_power_formula(1) returns 1

	17. we remove special_power_formula(1) from the call stack.
	18. we return to code: special_power_formula(2) the next value in the call_stack.
	19. we return to the return statement: n ** n + special_power_formula(n - 1)
	20. we substitute values: n = 2, special_power_formula(1) = 1.
	21. 2 ** 2 + 1 = 5, special_power_formula(2) returns 5

	22. we remove special_power_formula(2) from the call stack.
	23. we return to code: special_power_formula(3) the next value in the call_stack.
	24. we return to the return statement: n ** n + special_power_formula(n - 1)
	25. we substitute values: n = 3, special_power_formula(2) = 5.
	26. 3 ** 3 + 5 = 32, special_power_formula(3) returns 32

	27. we remove special_power_formula(3) from the call stack.
	28. we return to code: special_power_formula(4) the next value in the call_stack.
	29. we return to the return statement: n ** n + special_power_formula(n - 1)
	30. we substitute values: n = 4, special_power_formula(3) = 32.
	31. 4 ** 4 + 32 = 288, special_power_formula(4) returns 288

	32. we remove special_power_formula(4) from the call stack.
	33. we return to where special_power_formula(4) was first called in the main code returning: 288	

Why would I ever use the recursion technique?  Many problems do not require it and most can be 
solved with iteration.  There are subsets of problems that recursion works very well at:

	Going through a tree structure.  Imagine you have:

		hospitals > departments > sub-departments > patients

	If you want a list of patients and only could use iteration, you'd have to go through 
	all departments, add them to a list and then iterate over the list.  Recursion can
	solve the same problem with only a few lines of code.

	Going through a social network.  

		friends -> friends -> friends ...

	Where does the friend network end?  2-3...8 deep.  Breadth first search and depth first
	search are 2 special recursive algorithms.

	Another great algorithm to look up:

		Tower of Hanoi

	Also:

		Sudoku

	You can solve sudoku with recursion.  It's probably easier to do so than to use iteration!

"""

raw_input(prompt)


#!/usr/bin/env python
import sys
 
sys.setrecursionlimit(5000)
 
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
 
print factorial(3000)


prompt="""
If you comment out the code sys.setrecursionlimit(5000).
This will fail!  Python only allows a few thousand calls to be 
recorded on the call stack!  To increase this, we need
to set the limit using sys.

Note, if there is no break condition, you will get infinite
recursion and hit that call stack limit sooner than later.

This is good as storing things on the stack (temp var, location etc)
costs memory.  Infinite calls would require infinite memory (and time).
"""

raw_input(prompt)