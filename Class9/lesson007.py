prompt="""
MRO
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
Inheritance and Classes
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

prompt="""
Inheritance and Classes
"""

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
Inheritance and Classes
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
Inheritance and Classes
"""

