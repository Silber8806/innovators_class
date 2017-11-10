total_orders = 5
cheese_qty = 2
pasta_qty = 3
sauce_qty = 1

total_produced = 0
current_order = 0
while(current_order < total_orders):
	current_order += 1
	print
	order = raw_input("choose cheese/pasta/sauce?")

	if (order == 'cheese'):
		total_prod = cheese_qty
		total_produced += cheese_qty
	elif (order == 'pasta'):
		total_prod = pasta_qty
		total_produced += pasta_qty		
	elif (order == 'sauce'):
		total_prod = sauce_qty
		total_produced += sauce_qty	
	else:
		print("failed order...")
		current_order -= 1

	if (order == 'cheese' or order == 'pasta' or order == 'sauce'):
		prod = 0
		while(prod < total_prod):
			print(order)
			prod += 1

print("Factory done!")
print("Total Production: %s" % total_produced)