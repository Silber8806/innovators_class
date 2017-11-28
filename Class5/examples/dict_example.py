# Author: Marissa Fisher

d = {'red': 1, 'green': 2, 'blue': 3, 'purple': 4}

color_list = ['red', 'pink', 'yellow', 'blue', 'green', 'orange', 'purple']

for color in color_list:
    if color in d:
        print(color+' '+str(d[color]))



