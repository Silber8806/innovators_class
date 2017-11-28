# Author: Marissa Fisher

word_list = [
    ('mood', 'doom'),
    ('apple', 'core'),
    ('race', 'care'),
    ('evil', 'live'),
    ('spam', 'maps')
]

for i in range(len(word_list)):
    if word_list[i][0] == word_list[i][1][::-1]:
        print(str(word_list[i]) + ' is a reverse pair.')
    else:
        print(str(word_list[i]) + ' is not a reverse pair.')
