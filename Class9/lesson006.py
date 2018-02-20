prompt="""
Let's begin this next lesson on inheritance with
just a class and an instance.  We will then develop
a method of sharing attributes and methods between
different classes.
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
In the above, we have a Person class, which
can introduce itself using it's name.
Pretty simple.
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
In the above, we have an employee class, which 
references in it's parameter: Person.

This is called inheritance.  In inheritance, one
class inherits all the methods and attributes 
of a parent class.

In this case, Employee inherits the introduction
method.
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
Notice, we can inherit from many different sources.
This is called multiple inheritance.  Note, not 
all computer languages support multiple inheritance.

Java for example, has only single inheritance, but has
a concept of interfaces (I concept that doesn't exist
in Python)
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
The last example shows that inheritance is hierachial.
You can have a CEO that inherits from Employee, which
inherits from person.  All the methods are combined
in the CEO clasa.

CEO in the above case can:
> Make introductions like any other person.
> Get a raise like any employee.
> make personal speeches, which is something only CEOs can do?
"""

raw_input(prompt)

