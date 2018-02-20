prompt="""
Imagine if we took a bunch of variable and functions.
We associated them to a single variable as a collection.
That's the idea behind an object!
"""

raw_input(prompt)

def create_car(car_id,model,make,year,price,seats=4):

	car = {
		"id" : car_id,
		"model": model,
		"make" : make,
		"year" : year,
		"price": price,
		"seats": seats
	}

	return car

prompt="""
What is the object analog of our create car statement!
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
Before we can create an object, we need to define it (like def statement).
To do this, we create a class, which can be seen as a template for an objects!

The above is a Car Class, which will produce Car objects or instances.  The
__init__ function is called the constructor.  It's what is used to create 
a car object!  
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
When we call Car(<parameters>) it creates a car object 
and associates it with car1 variable.

We can now use <object>.<variable> to retrieve any
of the attributes.  This is more substinct then
using a dictionary.  

From this point on we will call an 
object's variables: object attributes.
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
		print(self)

print
print("Class:")
print(Car)

print
print("Instance 1:")
car1 = Car(1,'Ford','Mustang','2010','35000',4)
print(car1)

print
print("Instance 2:")
car2 = Car(2,'Chevrolet','Camaro','2008','21000',4)
print(car2)

prompt="""
Did you notice the term self?

I print self inside the class constructor.  It returns
a memory reference.  You'll notice self and the car 
instances share the same reference.

That reference is different between cars (instances)!

When you construct 2 cars, both entities are different
objects!  All variables associated with it occupy 
different spaces as well (in-theory).
"""

raw_input(prompt)

print
print("This is a car report:")
print("car id: %s" % car1.car_id)
print("make: %s" % car1.make)
print("model: %s" % car1.model)
print("year: %s" % car1.year)
print("price: %s" % car1.price)
print("seats: %s" % car1.seats)
print
print("This is a car report:")
print("car id: %s" % car2.car_id)
print("make: %s" % car2.make)
print("model: %s" % car2.model)
print("year: %s" % car2.year)
print("price: %s" % car2.price)
print("seats: %s" % car2.seats)

prompt="""
A cars attributes are independently retrieable using the 
<object>.<variable> notation.  Notice how return type 
is completely dependent on <object> attribute.
"""

raw_input(prompt)

car1.seats=100
car2.seats=40

print
print("modified")
print("seats: %s" % car1.seats)
print("seats: %s" % car2.seats)

prompt="""
You can modify attributes using the <object>.<attribute> = <statement/value>
notation.  This is generally frowned upon!  More on this later!
"""

raw_input(prompt)

