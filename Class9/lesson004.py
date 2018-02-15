prompt="""
The next lesson will cover the concept of 
inheritance!
"""

raw_input(prompt)

class pt:
	def __init__(self,x,y):
		self.x = x
		self.y = y

	def __repr__(self):
		return "(%s,%s)" % (self.x,self.y)

class vector(pt):
	def __add__(self,opp_pt):
		if (isinstance(opp_pt,vector)):
			self.x += opp_pt.x
			self.y += opp_pt.y
		return self

v1 = vector(1,1) 
v2 = vector(2,2)

v3 = v1 + v2 
print(v3)

prompt="""
Points should not change?  At least for this exercise (no change of coordinates).
We want them to be immutable.  To do this, we can get rid of the __add__ function.

A vector starting at the origin shares an (x,y) value with the concept of a point.
We, however, do want to be able to add to the vector other vectors!  We also
like the __repr__ function.

How can we start with the pt attributes/methods and then add custom methods to it
for vector.  We do this through the concept of inheritance.

Notice something different with the Vector class:

	class vector(pt):

It has a parameter.  The parameter happens to be the pt class.  When a class is listed
in the class parameters, it is called inheritance.  All methods/attributes of 
pt become adopted by vector.  Any methods and attributes found in vector are added
after the fact!
"""

raw_input(prompt)

class person():
	def __init__(self,name):
		self.name

	def get_name(self):
		return self.name

	def set_name(self,value):
		print("changing name...")
		self.name = value 
		return 0

	def __repr__(self):
		return str(self.name)

class employee(person):
	def __init__(self,name,employee_id, salary):
		self.name = name 
		self.employee_id = employee_id
		self.salary = salary

	def set_raise(self,percent):
		self.salary *= percent

	def __repr__(self):
		return str("angel corps:" + self.name)

class software_engineer(employee):
	def produce_software(self):
		print("I am buidling software...")
		return 0

	def build_software(self):
		print("I am building software...")
		return 0

	def test_software(self):
		print("I am testing software")
		return 0

	def deploy_software(self):
		print("I am deploying software...")
		return 0

	def create_software(self):
		self.produce_software()
		self.build_software()
		self.test_software()
		self.deploy_software()
		return 0

chris = software_engineer('chris',1,1000000)

print(chris.name)
print(chris.salary)
chris.set_raise(1.2)
chris.create_software()
print(chris.salary)

prompt="""
The next lesson will cover the concept of 
inheritance!
"""

raw_input(prompt)

class person():
	def __init__(self,name):
		self.name

	def get_name(self):
		return self.name

	def set_name(self,value):
		print("changing name...")
		self.name = value 
		return 0

	def __repr__(self):
		return str(self.name)

class employee(person):
	def __init__(self,name,employee_id, salary):
		self.name = name 
		self.employee_id = employee_id
		self.salary = salary

	def set_raise(self,percent):
		self.salary *= percent

	def __repr__(self):
		return str("angel corps:" + self.name)

class cybersecurity():
	def set_alert_level(self,alert):
		self.alert = alert
		return 0

class software_engineer(employee):
	def produce_software(self):
		print("I am buidling software...")
		return 0

	def build_software(self):
		print("I am building software...")
		return 0

	def test_software(self):
		print("I am testing software")
		return 0

	def deploy_software(self):
		print("I am deploying software...")
		return 0

	def create_software(self):
		self.produce_software()
		self.build_software()
		self.test_software()
		self.deploy_software()
		return 0


class cybersecurity_engineer(software_engineer,cybersecurity):
	pass

chris = cybersecurity_engineer('chris',1,1000000)

print(chris.name)
print(chris.salary)
chris.set_raise(1.2)
chris.create_software()
print(chris.salary)
chris.set_alert_level("warning")
print(chris.alert)


prompt="""
The above shows a technique called multiple inheritance.  We 
can combine both the software engineer methods/attributes as 
well as the cybersecurity ones to create a new role:

	cybersecurity_engineer

This is kind of interesting!
"""

raw_input(prompt)


class person(object):
	def __init__(self,name):
		self.name

	def get_name(self):
		return self.name

	def set_name(self,value):
		print("changing name...")
		self.name = value 
		return 0

	def __repr__(self):
		return str(self.name)

class employee(person):
	def __init__(self,name,employee_id, salary):
		self.name = name 
		self.employee_id = employee_id
		self.salary = salary

	def set_raise(self,percent):
		self.salary *= percent

	def __repr__(self):
		return str("angel corps:" + self.name)

class cybersecurity(object):
	def set_alert_level(self,alert):
		person.alert = alert
		return 0

class admin_policy(object):
	def set_alert_level(self,peep,alert):
		peep.alert = alert
		return 0

class software_engineer(employee):
	def produce_software(self):
		print("I am buidling software...")
		return 0

	def build_software(self):
		print("I am building software...")
		return 0

	def test_software(self):
		print("I am testing software")
		return 0

	def deploy_software(self):
		print("I am deploying software...")
		return 0

	def create_software(self):
		self.produce_software()
		self.build_software()
		self.test_software()
		self.deploy_software()
		return 0


class cybersecurity_engineer(software_engineer,cybersecurity):
	pass

class system_administrator(employee, admin_policy,cybersecurity):
	pass

chris = system_administrator('chris',1,1000000)
johny = cybersecurity_engineer('johny',2,2000000)


chris.set_alert_level(johny,'high alert')
print(johny.alert)
johny.set_alert_level("no alert")
print(johny.alert)

prompt="""
What if two methods conflict with each other during multiple inheritance?
Then the class furtherest left in the parameters dominates.
"""

raw_input(prompt)

