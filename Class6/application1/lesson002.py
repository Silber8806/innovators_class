prompt = """
JAVASCRIPT OBJECT NOTATION.

JSON can be thought of as a hierarchial set 
of lists and dictionaries.

Example:

[
	"first name":"Chris",
	"last name": "Kottmyer",
	"Hobbies : [
		"Reading",
		"Writing",
		"Sleeping",
		"Coding"
	]
]

JSON can be very complex.

The example above could be part of my Facebook profile.
We could even add posts to the JSON object!

[
	"first name":"Chris",
	"last name": "Kottmyer",
	"Hobbies : [
		"Reading",
		"Writing",
		"Sleeping",
		"Coding"
	],
	posts : [
			{
				"header" : "Learn Python",
				"body": "I am learning Python today!",
				"images": [
					1,2,3
				]
			},
			{
				"header" : "Learn Python 2 ",
				"body" : "I am learning Python tomorrow!",
				"images" : [
					4,5,6
				]
			}
	]
]

JSON can be deeply nested representing attributes and collections
of objects.

This naturely translates to dictionaries and lists in python!
"""

raw_input(prompt)

import json

json_file = 'death.data'

print("Contents of File:")
print(open(json_file,'r').read())

prompt = """
The first step in manipulating a JSON file is to open it as
a regular file and read it's content as a string.

At this stage, you should look at the structure of the data
and try to find patterns that you can later exploit!

Later on, we will convert the string to a set of dictionaries
and lists using the json library!
"""

raw_input(prompt)

