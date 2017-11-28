print("This is a zip")

states = ["MA","RI","NH","NM"]
state_dict = {"MA": "Massachusetts",
			  "RI":"Rhode Island", 
			  "NH":"New Hampshire", 
			  "NM": "New Mexico"}

state_names = [state_dict[s] for s in states]
print("Use the state dict to create a named list of states")
print(state_names)

print
print("we can pair up state abbre with state names using zip:")
state_abbreviations = zip(state_names,states)
print(state_abbreviations)

print
print("This is a short cut for:")
original_zip = []
for indice in range(0,len(states)):
	original_zip.append((state_names[indice],states[indice]))
print(original_zip)


