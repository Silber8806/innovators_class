print("This is a set:")

universe = ["Earth", "Mars", "Moon", "Moon", "Moon"]

print(universe)

unique_universe = set(universe)
print
print("set is a unique set of keys.")
print(unique_universe)

print
print("We can add a member using add command:")
unique_universe.add("Pluto")
print(unique_universe)

print
print("We can test for basic membership using in:")
print("Pluto" in unique_universe)

print
print("sets are used mostly for doing set operations")
earth = set(["Earth"])

print
print("Is earth a subset of the universe")
print(unique_universe.issubset(earth))

print
print("Is the earth a superset of the universe")
print(unique_universe.issuperset(earth))

print
print("what does earth and the universe have in common.")
print(unique_universe.intersection(earth))

print
print("What is the union of two systems:")
mercury = set(["Mercury"])
print(unique_universe.union(mercury))

print
print("What are not shared between earth and mercury")
print(earth.symmetric_difference(mercury))