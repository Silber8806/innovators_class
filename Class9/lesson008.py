prompt="""
MRO
"""

import datetime

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

