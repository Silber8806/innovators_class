prompt="""
Attributes are the equivalent of dictionary keys 
in lesson001.  How would you model ignite, car_report
and car_make_and_model functions?
"""

raw_input(prompt)

def ignite_camaro():
	print "Vroom Vroom"

def ignite_mustang():
	print "Vroom VROOOOOOOOOOOMMMMMMMMMMMMM!"

def car_report(**car_dict):
	for trait, trait_value in car_dict.iteritems():
		print(trait,trait_value)
	return None

def car_make_and_model(d,model,make):
	return d['model'] + " " + d['make']


prompt="""
We can define functions associated with an object by defining
them within a class.  The only difference is that the keyword
self is added to this.
"""

raw_input(prompt)

class Car:
	def __init__(self,car_id, model,make,year,price,seats=4):
		self.car_id = car_id
		self.model = model
		self.make = make
		self.year = year
		self.price = price 
		self.seats = seats

	def ignite(self):
		if (self.make == 'Mustang'):
			print("Vroom VROOOOOOOOOOOMMMMMMMMMMMMM!")
		elif (self.make) == 'Camaro':
			print("Vroom Vroom!")
		else:
			print("Vroom!")

	def car_report(self):
		print(self.car_id)
		print(self.model)
		print(self.make)
		print(self.year)
		print(self.price)
		print(self.seats)
		return None


prompt="""
We can define functions associated with an object by defining
them within a class.  The only difference is that the keyword
self is added to this.
"""

raw_input(prompt)

car1 = Car(1,'Ford','Mustang','2010','35000',4)
car2 = Car(2,'Chevrolet','Camaro','2008','21000',4)

car1.ignite()
car2.ignite()

prompt="""
We can call the functions bound to a object by using . notation:
<object>.<func>(<parameters>).  

What about the self parameter?  The self parameter is supplied 
by the <object> portion of this call.  
"""

raw_input(prompt)

print
car1.car_report()
print
car2.car_report()

prompt="""
We don't need to add a dictionary to the car_report call.  It's provided
by the object itself.  This is called encapsulation.  We can't see 
all the data inside car1 or car2, but the function itself has access to it.
"""

raw_input(prompt)

class Car:
	def __init__(self,car_id, model,make,year,price,seats=4):
		self.car_id = car_id
		self.model = model
		self.make = make
		self.year = year
		self.price = price 
		self.seats = seats

	def ignite(self):
		if (self.make == 'Mustang'):
			print("Vroom VROOOOOOOOOOOMMMMMMMMMMMMM!")
		elif (self.make) == 'Camaro':
			print("Vroom Vroom!")
		else:
			print("Vroom!")

	def car_report(self):
		print(self.car_id)
		print(self.model)
		print(self.make)
		print(self.year)
		print(self.price)
		print(self.seats)
		return None

	def __repr__(self):
		return str(self.car_id) + ":" + self.model + " " + self.make

car3 = Car(1,'Ford','Mustang','2010','35000',4)
car4 = Car(2,'Chevrolet','Camaro','2008','21000',4)

print
print("unmodifed:")
print(car1)
print(car2)
print
print("modifed:")
print(car3)
print(car4)
print

prompt="""
car_make_and_model function describes each car well!  It would be 
useful if when we printed the car, it would print the make and model!
We could even add car_id into it!

__repr__ has to return a string.  It is what print uses when it prints
an object!
"""

raw_input(prompt)



