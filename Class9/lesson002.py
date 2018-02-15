prompt="""
Do you remember how to create a car in the previous 
example?
"""

raw_input(prompt)

def create_car(car_id, model,make,year,price,seats=4):
	car = [car_id, model, make, seats, price]
	return car

prompt="""
That's right, we used a function!  We can mimic this
by creating a class!
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

prompt="""
The above is called a class!  It behaves similarly to create_car
function in that it takes some parameters and creates a new object.
The function creates a list.  The class creates an instance.

The function that creates a new "Instance" is called a construction
and in python it's represented by the function __init__.  There is
a special word in the __init__ function.  It is called 
self.  Self is a reference to the object being created.  

Since a class can make many instances, self will be specific to
the instance being created.  We will look into this more!
"""

raw_input(prompt)


car1 = Car(1,'Ford','Mustang','2010','35000',4)

print("This is a car report:")
print("car id: %s" % car1.car_id)
print("make: %s" % car1.make)
print("model: %s" % car1.model)
print("year: %s" % car1.year)
print("price: %s" % car1.price)
print("seats: %s" % car1.seats)

prompt="""
We finally create our Car object called car1.
We pass it a set of values into Car, which 
invokes our Car's __init__ function.  This 
returns a new Car object (implied).

We can retrieve any variable associated with 
car1 using the car1.<variable> notation.  
"""

raw_input(prompt)

car1 = Car(1,'Ford','Mustang','2010','35000',4)

print
print("This is a car report:")
print("car id: %s" % car1.car_id)
print("make: %s" % car1.make)
print("model: %s" % car1.model)
print("year: %s" % car1.year)
print("price: %s" % car1.price)
print("seats: %s" % car1.seats)
print

car2 = Car(2,'Chevrolet','Camaro','2008','21000',4)

print("This is a car report:")
print("car id: %s" % car2.car_id)
print("make: %s" % car2.make)
print("model: %s" % car2.model)
print("year: %s" % car2.year)
print("price: %s" % car2.price)
print("seats: %s" % car2.seats)

car1.seats=100
car2.seats=40

print("car1 seats: %s" % car1.seats )
print("car2 seats: %s" % car2.seats )

prompt="""
Notice how each car has it's own set of variables after
construction?  This is one of the useful features of
objects.  Can you modify them independently?

The answer is, yes you can.  Each variable is separate
from each other, but bound to the cars they were 
initiated with.  This is what the self key does (binds)
the variable to an object.
"""

raw_input(prompt)

print(Car)
print(car1)
print(car2)

prompt="""
Let's do a little experiment!

When printing the Car class it just says:

	__main__.Car

When we print the instance, we get:

	<__main__.Car instance at <memory address>>

Notice, that both car1 and car2 have different
memory addresses!  They are not the same object!
"""

raw_input(prompt)

class Car:
	def __init__(self,car_id, model,make,year,price,seats=4):
		print(self)
		self.car_id = car_id
		self.model = model
		self.make = make
		self.year = year
		self.price = price 
		self.seats = seats

print("experiment:")
car3 = Car(1,'Ford','Mustang','2010','35000',4)
print(car3)

car4 = Car(1,'Ford','Mustang','2010','35000',4)
print(car4)

prompt="""
What about if we modify the constructor to print(self).
Then we create a new instance car3 and print(car3).

Notice how the memory address is the same value?  It's the
same object.  What if we made another car?  car4?

car3 and car4 are different.  Self always references the 
object that was created!  self therefore references whatever
object it was embedded in!
"""

raw_input(prompt)

def car_report(car_id, model,make,year,price,seats):
	print("This is a car report:")
	print("car id: %s" % car_id)
	print("make: %s" % make)
	print("model: %s" % model)
	print("year: %s" % year)
	print("price: %s" % price)
	print("seats: %s" % seats)
	return 0


class Car:
	def __init__(self,car_id, model,make,year,price,car_report,seats=4):
		self.car_id = car_id
		self.model = model
		self.make = make
		self.year = year
		self.price = price 
		self.seats = seats
		self.car_report = car_report

new_car = Car(1,'Ford','Mustang','2010','35000',car_report,4)
new_car.car_report(new_car.car_id, new_car.model,new_car.make,new_car.year,new_car.price,new_car.seats)

prompt="""
The above is confusing!  car report is an attribute of Car, but we have to make a reference to new_car 
every function call.  That would be counter productive if we wanted to keep Car's associated with
it's functions and use the self construct!
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
		self.car_report = car_report

	def best_car_report(self):
		print("This is a car report:")
		print("car id: %s" % self.car_id)
		print("make: %s" % self.make)
		print("model: %s" % self.model)
		print("year: %s" % self.year)
		print("price: %s" % self.price)
		print("seats: %s" % self.seats)		
		return 0

newer_car = Car(1,'Ford','Mustang','2010','35000',4)
newer_car.best_car_report()

prompt="""
WOW!  How simple that function call is?  car_report function has 
access to all the variables of a specific object through the 
self keyword.  We therefore don't need any parameters for them!

More importantly, all cars have car_report functions that only
access there specific car variables.  Let's talk about terminology:

Attribute - A variable that is bound to a specific object.
Method - A functon that is bound to a specific object.

Note, everytime we create an object, it creates new attributes 
and functions.  They are not the same thing!!! 
"""

raw_input(prompt)

newest_car = Car(1,'Ford','Mustang','2010','35000',4)

print("car function:")
print(car_report)
print("car function as an attribute:")
print(new_car.car_report)
print("car method of newer_car:")
print(newer_car.best_car_report)
print("car method of newest_car:")
print(newest_car.best_car_report)

prompt="""
To confirm this, let's look at all the methods and functions declared 
for car report:

The function defined outside the class and passed in as a part of the 
constructor have the same memory address.

The funtions have the same memory address.  Methods don't!

Note, this is not always true for attributes as Python keeps small
numbers and certain permutation of strings in a single memory space
to optimize memory usage.
"""

raw_input(prompt)

