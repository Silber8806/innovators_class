# Author: Marissa Fisher

class_list = ['Eric', 'Alyssa', 'John', 'Megan']

for i in range(len(class_list)):
    class_list[i].lower()

print(class_list)
print('No change here!')

for i in range(len(class_list)):
    class_list[i] = class_list[i].lower()

print(class_list)



