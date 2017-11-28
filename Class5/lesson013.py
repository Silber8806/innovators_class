# dictionary is a mapping of a key to a value.

oxford_dict = {"Hello":"an expression or gesture of greeting"}

print("This is a dictionary")
print(oxford_dict)

print
print("We can add new 'words' (keys) to it.")
oxford_dict["World"] = "the earth with its inhabitants and all things upon it"
print(oxford_dict)

print
print("Dictionaries are unique key => value pairs")
oxford_dict["World"] = 5
print(oxford_dict)

print
print("You can also see keys as custom indexes...")
print(oxford_dict["World"])

print
print("You use dict[<key>] notation to retrieve values")
print(oxford_dict["Hello"])

print
print("dictionaries can hold lists, dicts and other objects")
oxford_dict["Countries"] = ["Germany","Canada","China","USA"]

print("They are also mutable...")
webster = oxford_dict
oxford_dict["Hello"] = "AOL: Goodbye!"
print(webster)


