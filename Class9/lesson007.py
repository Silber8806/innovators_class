prompt="""
We will briefly touch the concept of composition
by first going through a problem fixed by something
called the Method Resolution Order (MRO).
"""

raw_input(prompt)

class SecretAgent:
	def __init__(self,name):
		self.name = name 

	def steal_information(self):
		print("I Stole Info!")

	def introduction(self):
		print("I am a secret agent!")

raw_input(prompt)

class Employee1(Person,SecretAgent):
	def __init__(self,name):
		self.name = name

class Employee2(SecretAgent,Person):
	def __init__(self,name):
		self.name = name

print
Jane = Employee1("Jane")
Jane.steal_information()
Jane.introduction()

print
Jane = Employee2("Jane")
Jane.steal_information()
Jane.introduction()
print

prompt="""
We have 2 types of employees above!  The first
type of employee inherits from person first, while
the second inherits from secret agent.  Both:
Person and Secret Agent have a introduction method!

Which one will be called by each employee?  In 
multiple inheritance, the left most class always 
has precedence!

This is general not a good thing?  There is a good
chance we unintentionally overwrite methods!
"""

raw_input(prompt)

class Introductions:
	def __init__(self):
		pass

	def make_introduction(self,greeting_type,name=None):
		if (greeting_type == "secret agent"):
			print("I am a secret agent!")
		else: 
			if (name is not None):
				print("My name is %s" % name)
			else:
				print("hi")

class Employee:
	def __init__(self,name,agent):
		self.name = name
		self.agent_type = agent

	def set_introductions(self,intro):
		self.introductions = intro

	def introduction(self):
		self.introductions.make_introduction(self.agent_type,name)
		return 0


Jane = Employee("Jane","standard")
John = Employee("John","secret agent")

print
print("Jane interaction:")
Jane.set_introductions(introductions)
Jane.introductions()

print
print("John interactions:")
John.set_introductions(introductions)
John.introductions()

prompt="""
Alright, so how can we customize the behavior of the introductions
so that they behave properly.  The answer is we don't use inheritance.

We use the concept of composition.  That is, we have 2 unrelated classes,
which interact with each other through methods.

In our exmaple, we have Introduction class and a Employee class.  We 
then use the introduction method to call the make_introductions method
in Introductions.  This results in isolating changing code in one place
and not having to consolidate or keep track of changes in inheritance
(if they will get overwritten...).
"""

raw_input(prompt)

class Introductions:
	def __init__(self):
		pass

	def make_introduction(self,greeting_type,name=None):
		if (greeting_type == "secret agent"):
			print("I am a secret agent!")
		else: 
			if (name is not None):
				print("My name is %s" % name)
			else:
				print("hi")

class Employee:
	def __init__(self,name):
		self.name = name
		self._agent_type = 'secret agent'
		self._set_introductions()

	def get_agent_type(self):
		return self.agent_type

	def set_agent_type(self,value):
		self.agent_type = value
		return value 

	def _set_introductions(self):
		self.introductions = Introductions()

	def introduction(self):
		self.introductions.make_introduction(self.agent_type,name)
		return 0

Jane = Employee("Jane")
John = Employee("John")

print
print("Jane interaction:")
Jane.get_agent_type()
Jane.introductions()

print
print("John interactions:")
John.get_agent_type()
John.set_agent_type("secret agent")
John.get_agent_type()
John.introductions()


prompt="""
We modify hte above code to set introductions during the employee creation 
process.  That simplifes the code above.
"""

