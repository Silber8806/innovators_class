clients = {"Target": [1000,True], "Sears": [200, False],"Macy's":[250, True]}

print
print("Check for key existence:")
if(clients.has_key("Target")):
	sales=clients["Target"][0]
	repeat=clients["Target"][1]
	if(repeat):
		print("Target resell: %s" % sales)

print
print("Check a bunch of keys...")
opportunities=["Target","Sears","Walmart"]
for opportunity in opportunities:
	if opportunity not in clients.keys():
		print("new client: %s" % opportunity)
	else:
		print("old client: %s" % opportunity)

print
print("going through all relationships:")
for client,data in clients.items():
	if (data[0]<500 and client != "Sears"):
		print("Less than $500 in sales")
		print("Not special client Sears!")
		print(client)