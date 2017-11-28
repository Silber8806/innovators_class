market_basket = {}

market_basket["apple"] = 3
market_basket["oranges"] = 1
market_basket["cookies"] = "N/A"

print("dictionary:")
print(market_basket)

print
print("Decomposing keys, cookies and relationships!")
print("Keys:")
print(market_basket.keys())
print("""
***
	Note: Keys have no order.
	Calling market_basket.keys()
	might change the order of values.
***
""") 

print
print("Values:")
print(market_basket.values())

print
print("Relationships:")
print(market_basket.items())



