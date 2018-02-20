prompt="""
Before we talk about classes, instances and inheritance, we will do a
imperative example.
"""

raw_input(prompt)

import random

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

def create_price(base,min_flux,max_flux):
	return base + random.randint(min_flux,max_flux)

def car_factory():
	car_id = range(1,101)
	make = str('Chevrolet,' * 50 + 'Ford,' * 50)[:-1].split(',')
	model = str('Camaro,' * 50 + 'Mustang,' * 50)[:-1].split(',')
	year = map(lambda x : random.randint(1999,2018), range(101))
	seats = ("4," * 100)[:-1].split(',')
	prices = map(lambda x: create_price(50000,-5000,5000),range(51)) + map(lambda x: create_price(30000,-3000,5000),range(51))
	car_parts = zip(car_id, make, model, year, prices,seats)
	new_cars = map(lambda x: create_car(*x),car_parts)
	return new_cars

new_cars = car_factory()

print
print("cars:")
for car in new_cars:
	print(car)
print

prompt="""
The above is custom code to create 100 cars: 50 mustangs and 50 camaros!
We invoke the car creation with the car factory!
"""

raw_input(prompt)

def ignite_camaro():
	print "Vroom Vroom"

def ignite_mustang():
	print "Vroom VROOOOOOOOOOOMMMMMMMMMMMMM!"

for car in new_cars:
	if car['make'] == 'Mustang':
		car["engine"] = "V8"
		car["ignite"] = ignite_mustang
		car["ignite"]()
	if car['make'] == 'Camaro':
		car['seats'] = 2
		car["ignite"] = ignite_camaro
		car["ignite"]()

prompt="""
We can add custom features to the car after creating them.  We 
just create new keys and associate them.
"""

raw_input(prompt)

def car_report(car_dict):
	for trait, trait_value in car_dict.iteritems():
		print(trait,trait_value)
	return None

def car_make_and_model(d,model,make):
	return d['model'] + " " + d['make']

for car in new_cars:
	car['report'] = car_report
	car['type'] = car_make_and_model
	car['report'](car)
	car['type'](car,car['model'],car['make'])


prompt="""
Now the complexity starts revealing itself!  car_make_and_model
is completely dependent on d.  Where d is always the dictionary
holding car information.

The complexity will only continue to grow!  
"""

raw_input(prompt)

