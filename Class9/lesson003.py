prompt="""
objects are definition first class members and
can be used in arrays, passed into functions 
or even be used to instantiate other instances
(from the same or other classes).
"""

raw_input(prompt)

class pt:
	def __init__(self,x,y):
		self.x = x
		self.y = y

origin = pt(0,0)
print(origin)

pts = [(x,y) for x in range(-10,10) for y in range(-10,10)]

print("pts on graph:")
print(pts)

graph_maker = lambda x,y : pt(x,y)
graph = [graph_maker(x,y) for x,y in pts]

print("actual graph construct!")
print(graph)

prompt="""
Above, we first iterate over all points on a graph (integer only) between
x = (-10, 10) and y = (-10 , 10).  We print this!

We then feed the (x,y) coordinates to a graph_maker function, which creates 
a graph of points.  When we print this, we see the (x,y) coordinates have
been converted to 100 pt objects.

That looks ugly though!
"""

raw_input(prompt)

class pt:
	def __init__(self,x,y):
		self.x = x
		self.y = y

	def __repr__(self):
		return "(%s,%s)" % (self.x,self.y)

pts = [pt(x,y) for x in range(-10,10) for y in range(-10,10)]

print(pts)


prompt="""
Alright, let's consolidate a bit.  We use a new function called:

	__repr__

Why the double underscore?  These are called magic methods!  
Magic methods are attached to symbols (+,- signs), special 
functions (print) or specific methods!  

	__repr__ 

means representation.  The result of __repr__ has to be a string
and it is what the print function returns for an object (when printed).
"""

raw_input(prompt)

class pt:
	def __init__(self,x,y):
		self.x = x
		self.y = y

	def __repr__(self):
		return "(%s,%s)" % (self.x,self.y)

	def __add__(self,opp_pt):
		if (isinstance(opp_pt,tuple)):
			x, y = opp_pt 
			self.x += x
			self.y += y
		elif (isinstance(opp_pt,pt)):
			self.x += opp_pt.x
			self.y += opp_pt.y
		return (self.x,self.y)


pts = [pt(x,y) for x in range(-10,10) for y in range(-10,10)]

solution = pt(1,1) + (2,2)
print(solution)

solution = pt(1,1) + pt(2,2)
print(solution)

prompt="""
We added another function __add__.  This is the 
addition symbol (+)?  

In my specific version of the function, I can either 
"add" a tuple or a pt to another pt!  
"""

raw_input(prompt)

class pt:
	def __init__(self,x,y):
		self.x = x
		self.y = y

	def __repr__(self):
		return "(%s,%s)" % (self.x,self.y)

	def __add__(self,opp_pt):
		if (isinstance(opp_pt,tuple)):
			x, y = opp_pt 
			self.x += x
			self.y += y
		elif (isinstance(opp_pt,pt)):
			self.x += opp_pt.x
			self.y += opp_pt.y
		return pt(self.x,self.y)


solution = pt(1,1) + pt(2,2) + pt(-3,-3)
print(solution)

prompt="""
We can't add 3 points in the original code.  The return
of __add__ was a tuple.  We want to it to return a pt
instead, which we can use with other points in the future.

This allows us to add 3 points and return a new point, which
can be used with other future points!
"""

raw_input(prompt)


class pt:
	def __init__(self,x,y):
		self.x = x
		self.y = y

	def __repr__(self):
		return "(%s,%s)" % (self.x,self.y)

	def add(self,x,y):
		self.x += x
		self.y += y
		return self

	def __add__(self,opp_pt):
		if (isinstance(opp_pt,tuple)):
			x, y = opp_pt 
			self.x += x
			self.y += y
		elif (isinstance(opp_pt,pt)):
			self.x += opp_pt.x
			self.y += opp_pt.y
		return self


solution = pt(1,1)
print(solution)


prompt="""
We can combine magic methods with standard methods
as long as the return of add is also a pt!
"""

raw_input(prompt)


class pt:
	def __init__(self,x,y):
		self.x = x
		self.y = y

	def __repr__(self):
		return "(%s,%s)" % (self.x,self.y)

	def add(self,x,y):
		self.x += x
		self.y += y
		return self 

	def __add__(self,opp_pt):
		if (isinstance(opp_pt,tuple)):
			x, y = opp_pt 
			self.x += x
			self.y += y
		elif (isinstance(opp_pt,pt)):
			self.x += opp_pt.x
			self.y += opp_pt.y
		return self


solution = pt(1,1).add(1,1).add(1,1).add(1,1)
print(solution)


prompt="""
Wait, why is the method being called over and over again?
How can that be possible?  Welcome to the concept of 
chaining!

If you return self for a function, you are returning the reference
to the object itself!  That object contains add method.  You can
then call add again!

Remember self is just a reference to an object!
"""

raw_input(prompt)
