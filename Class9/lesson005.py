prompt="""
Let's do another exercise pts on a graph!
"""

raw_input(prompt)

class vector:
	def __init__(self,x,y):
		self.x = x
		self.y = y

	def add(self,x,y):
		self.x = self.x + x
		self.y = self.y + y
		return self

	def multi(self,scalar)::
		self.x = self.x * scalar
		self.y = self.y * scalar
		return self

	def __repr__(self):
		return "(%s,%s)" % (self.x,self.y)

print
print("Simple addition:")
vec = vector(1,1)
vec.add(1,1)
print(vec)

print
print("Chained functions!")
vec = vector(0,0)
vec.add(1,1).add(2,2).add(3,3).add(4,4)
print(vec)
print

prompt="""

"""
raw_input(prompt)

print
print("Exotic chaining...")
vec = vector(0,0)
vec.multi(5).add(3,3).multi(5000)
print(vec)

vec = vector(0,0)
print(vec.multi(5).add(3,3).multi(5000).x)

prompt="""

"""
raw_input(prompt)

class vector:
	def __init__(self,x,y):
		self.x = x
		self.y = y

	def __mul__(self,scalar):
		self.x = self.x * scalar
		self.y = self.y * scalar
		return self

	def __add__(self,opp_vec):
		if (isinstance(opp_vec,vector)):
			self.x = self.x + opp_vec.x
			self.y = self.y + opp_vec.y
		return self

	def __repr__(self):
		return "(%s,%s)" % (self.x,self.y)

print
print("Origin:")
new_pt = pt(0,0)
new_pt + pt(1,1) + pt(2,2) + pt(3,3) * 1000
print(new_pt)
print 

print
print("Origin:")
new_pt = pt(0,0)
x_coords = (new_pt + pt(1,1) + pt(2,2) + pt(3,3) * 1000).x
print(x_coords)
print 

prompt="""
We can modify the previous calls to use magic methods as well!
"""
raw_input(prompt)
