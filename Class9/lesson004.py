prompt="""
Let's do another exercise pts on a graph!
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
This is every integer point between x => (-10,10) and y => (-10,10).
Nothing new yet!
"""

raw_input(prompt)

class pt:
	def __init__(self,x,y):
		self.x = x
		self.y = y
		return None

	def __mul__(self,scalar):
		self.x = self.x * scalar
		self.y = self.y * scalar
		return None

	def __repr__(self):
		return "(%s,%s)" % (self.x,self.y)

new_pt = pt(1,1)
new_pt * 1000
print
print("coordinates:")
print(new_pt)

prompt="""
We introduce a new concept.  Magic methods.  Magic methods are 
associated with symbols like: +, -, *, %.

__mul__ is multiply symbol: *
"""

raw_input(prompt)

class pt:
	def __init__(self,x,y):
		self.x = x
		self.y = y
		return None

	def __mul__(self,scalar):
		self.x = self.x * scalar
		self.y = self.y * scalar
		return None

	def __add__(self,opp_pt):
		if (isinstance(opp_pt,pt)):
			self.x = self.x + opp_pt.x
			self.y = self.y + opp_pt.y
		else:
			print("Unsupported operand: %s" % opp_pt)
			print("Only pts supported!")
		return None

	def __repr__(self):
		return "(%s,%s)" % (self.x,self.y)

origin = pt(0,0)

print
print("let's do some addition:")
origin + pt(1,1)
origin + pt(2,2)

print
print("The result:")
print(origin)

print
print("unsupported class:")
origin + "random!"
print 

prompt="""
__add__ is the + symbol.

We add one modifcation to the code!  The + 
symbol only works with other pt objects.

We do this by checking an objects class:

	isinstance(object,class)

This returns True if object's class == class specified.
"""

raw_input(prompt)

class pt:
	def __init__(self,x,y):
		self.x = x
		self.y = y

	def __repr__(self):
		return "(%s,%s)" % (self.x,self.y)

class vector:
	def __init__(self,x,y):
		self.x = x
		self.y = y

	def __mul__(self,scalar):
		self.x = self.x * scalar
		self.y = self.y * scalar
		return None

	def __add__(self,opp_pt):
		if (isinstance(opp_pt,pt)):
			self.x = self.x + opp_pt.x
			self.y = self.y + opp_pt.y
		else:
			print("Unsupported operand: %s" % opp_pt)
			print("Only pts supported!")
		return None

	def __repr__(self):
		return "(%s,%s)" % (self.x,self.y)

prompt="""
points on a graph shouldn't change.  They should be immutable.
Vector's on the otherhand can be multipled and added.  The references
x and y should change based on method calls.
"""

raw_input(prompt)

