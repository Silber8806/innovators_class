item_set = {"bloom", "zoom", "doom", "broom", "room"}

item_set.add("groom")

for i in item_set:
    i.replace("o", "O")

print(item_set)
print(len(item_set))

item_set = {["bloom", "zoom"], ["doom", "broom", "room"]}


for i in item_set:
    i.append("groom")

print(item_set)
print(len(item_set))



