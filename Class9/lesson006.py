prompt="""
Inheritance and Classes
"""

raw_input(prompt)

class Person:
	def __init__(self,name):
		self.name = name

	def introduction(self):
		print("My name is: %s" % self.name)
		return self.name

print
Jane = Person("Jane")
Jane.introduction()

prompt="""
Inheritance and Classes
"""

raw_input(prompt)

class Person:
	def __init__(self,name):
		self.name = name

	def introduction(self):
		print("My name is: %s" % self.name)
		return self.name

class Employee(Person):
	def __init__(self,name):
		self.name = name

print
Jane = Employee("Jane")
Jane.introduction()

prompt="""
Inheritance and Classes
"""

raw_input(prompt)

class Person:
	def __init__(self,name):
		self.name = name

	def introduction(self):
		print("My name is: %s" % self.name)
		return self.name

class SecretAgent:
	def __init__(self,name):
		self.name = name 

	def steal_information(self):
		print("I Stole Info!")

class Employee(Person,SecretAgent):
	def __init__(self,name):
		self.name = name

print
Jane = Employee("Jane")
Jane.steal_information()
Jane.introduction()

prompt="""
Inheritance and Classes
"""

raw_input(prompt)


class Person:
	def __init__(self,name):
		self.name = name

	def introduction(self):
		print("My name is: %s" % self.name)
		return self.name

class Employee(Person):
	def __init__(self,name,salary):
		self.name = name
		self.salary = salary

	def salary_raise(self,raise_pct):
		self.salary = self.salary * raise_pct

class CEO(Employee):
	def __init__(self,name,salary):
		self.name = name
		self.salary = salary

	def make_speech(self):
		print("AWESOME SPEECH!")

print
Jane = CEO("Jane",300000)
Jane.introduction()
Jane.salary_raise(1.2)
Jane.make_speech()
print
print(Jane.salary)


prompt="""
Inheritance and Classes
"""

raw_input(prompt)

