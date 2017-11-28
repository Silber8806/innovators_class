print
print("Testing for errors")

no_keys = {}

keys_to_try = ["Me","You"]

print(
"""
	try tests code block.
	If it errors, it executes
	the except block.
""")

for k in keys_to_try:
	try:
		no_keys[k]
	except:
		no_keys[k] = True

print("The result is:")
print(no_keys)

print
print("try should rarely be used.")
print("It can cover up unintentional errors.")


del no_keys["Me"]
del no_keys["You"]

print("You can delete a key using del keyword")
print(no_keys)