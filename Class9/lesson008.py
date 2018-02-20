prompt="""
The below is a more advanced case where I take the code 
from lesson 1 and write it in a more object-oriented 
way.  Notice, object-oriented code is often intuitive
and represent real world objects well.

In the below case, we have:

	Car
	Car Policies
	Factory

The factory creates cars.  It only controls the number
of cars being produced.

The Car Policy determins what cars are going to be 
produced and what the common features of the cars are.

The Car just takes arguments from the factory and 
produces a standard car.  After production, you 
can modify the attributes and use the attached methods.

This seems like a lot of code right?  Well, it is a lot
of upfront investment, but the result is the main 
function is unbelivably clean!

The other thing is, modifications, if isolated correctly
in classes are easier to maintain!

On the other hand, objects can also introduce complication.
The internal state of objects can sometimes cause hang-ups!

Overall, the below code is a signficant improvement in 
terms of readability and maintainance than lesson1 code!
"""

raw_input(prompt)

import datetime

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

class CarPolicies:
	def __init__(self,factory):
		self.factory = factory
		self.policy = factory.policy

	def set_factory_policy(self):
		if self.policy == 'mustang_policy':
			print('setting mustang policy')
			self._mustang_policy()
		elif self.policy == 'camaro_policy':
			print("setting camaro policy")
			self._camaro_policy()
		else:
			print("bad policy...")

	def _mustang_policy(self):
		factory = self.factory
		factory.model = 'mustang'
		factory.make = 'model'
		factory.year = datetime.datetime.now()
		factory.price = 35000
		factory.seats = 2
		return factory

	def _camaro_policy(self):
		factory = self.factory
		factory.model = 'camaro'
		factory.make = 'model'
		factory.year = datetime.datetime.now()
		factory.price = 20000
		factory.seats = 2
		return factory

	def __repr__(self):
		return "current policy is: %s" % self.policy


class CarFactory:
	def __init__(self):
		self.policy = 'mustang_policy'
		self.car_id = 0
		self.cars = []
		pass

	def set_policy(self,policy):
		self.policy = policy
		return 0

	def _create_car(self):
		new_car = Car(self.car_id, self.model,self.make,self.year,self.price,self.seats)
		return new_car


	def produce_cars(self,number):
		new_cars = []
		car_types = CarPolicies(self).set_factory_policy()
		print(self.model)
		print(self.make)
		print(self.year)
		print(self.price)
		print(self.seats)
		for n in range(number):
			self.car_id += 1
			new_cars.append(self._create_car())	
		self.cars.extend(new_cars)

	def __repr__(self):
		return (self.policy.replace('_policy',"")) + " factory" 


def main():
	Honda = CarFactory()
	Honda.produce_cars(50)
	Honda.set_policy('camaro_policy')
	Honda.produce_cars(50)
	print(Honda.cars)

main()

prompt="""
This is a more professionally done section, which shows 
more advanced code without getting into too much detail.

In the below classes, we have a Car, a Car Policy and 
a Car Factory.

Factories are production lines for any type of car.
They control production of cars.
"""

raw_input(prompt)

