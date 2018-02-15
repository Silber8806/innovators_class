prompt="""
Before we talk about objects, classes and inheritance.
Let's create motivation for the scenario using 
things that we have covered in previous classes.
"""

raw_input(prompt)

import random

def create_car(car_id, model,make,year,price,seats=4):
	car = [car_id, model, make, seats, price]
	return car

car_id = range(1,101)
make = str('Chevrolet,' * 50 + 'Ford,' * 50)[:-1].split(',')
model = str('Camaro,' * 50 + 'Mustang,' * 50)[:-1].split(',')
year = map(lambda x : random.randint(1999,2018), range(101))
seats = ("4," * 100)[:-1].split(',')

def create_price(base,min_flux,max_flux):
	return base + random.randint(min_flux,max_flux)

prices = map(lambda x: create_price(50000,-5000,5000),range(51)) + map(lambda x: create_price(30000,-3000,5000),range(51))

new_cars = zip(car_id, make, model, year, prices,seats)
new_cars = map(lambda x: create_car(*x),new_cars)
new_cars = {car[0]:car[1:] for car in new_cars}

prompt="""
We have a car factory!  It can produce 2 different models:

	Ford Mustang
	Chevrolet Camaro

Currently, we have 100 cars.  They are all provided to us 
as a dictionary with car_id being the key and value being 
a list of important values for the car, in this case:
	
	car_id
	model
	make
	year
	price
	seats

The position in the list indicates the value above.

We could in theory turn this into a dictionary as well to 
make it a bit easier.
"""

raw_input(prompt)

prompt="""
First question!  Is it intuitive?  
	
	new_cars - is a list of all new cars, that's intuitive.

I guess car_id is useful in this context, but the minute we 
start talking about possesion this analogy would collapse!

That said, it would be nice to just do something like this:

	print(car1.wheels)
	print(car2.make + " " + car2.model)

We could say the above code is somewhat intuitive!
"""

for car in new_cars.values():
	if car[1] == 'Mustang':
		car.append('V8')
		del car[3]

for car in new_cars.values():
	if car[1] == 'Camaro':
		car[-2] = 2

raw_input(prompt)


prompt="""
What if mustang had as a group had most 
traits in common with Camaro's, but varied
a bit differently!

We could for example, get rid of seats for mustang
and add engine to it.

We could also change the number of seats for the 
Camaro.

Sooner or later, all these changes will get confusing.
You'd have to read the code over and over again 
everytime you wanted to make a change.

Even if you used dictionaries, if you had 1000s of 
models and makes, it would get pretty confusing.  You'd 
need special functions just to read the dictionary or
list! 

None of this makes programming easier.  I means reading more
code.

There is also a trade-off here:
- Store each make-model separately and concat them during certain
operations.
- Store them the same, but use variables to determine how 
functions act on them.
"""

raw_input(prompt)

def ignite_camaro():
	print "Vroom Vroom"

def ignite_mustang():
	print "Vroom VROOOOOOOOOOOMMMMMMMMMMMMM!"

for car in new_cars.values():
	if car[1] == 'Mustang':
		car.append(ignite_mustang)

for car in new_cars.values():
	if car[1] == 'Camaro':
		car.append(ignite_camaro)


prompt="""
What if you had a function that applied to each car called ignite,
but due to how the key works, ignition is different for each 
model and make!

You don't want to store a separate function for each make and 
model.  That would be pretty confusing.  You'd have to memorize
many functions.

Simulaneously, if I wanted to pass in the make, model or seats 
into the function.  I'd have to always make a reference to the 
list being acted on!

What if the list or dictionary changed?  Do I really want to 
keep track of all of this!
"""

raw_input(prompt)

prompt="""
The reality is, we would be much happier if the functions and 
variables knew about each other.  Imagine a car that owned 
it's own variables and functions!  That's the concept behind 
a class and instance.

A class is a description of variables and functions owned
by a object like a car.  It's the template we use to 
initialize objects.

A instance is an actual object.  Like the members of 
new_car, they contain a custom set of variables and 
functions.  Unlike classes, we can change both the 
variables and functions while we are running the program.

Classes are only used to "create" objects.  Objects or 
instances are the actual things we interact with!

We will get into the details in the next lecture!
"""

raw_input(prompt)