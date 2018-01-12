prompt = """
Lesson 2 covers CSV data format.  

CSV is just a comma separated list
of values called attributes.  Where
each record is terminated by a 
newline character: \\n.

Data format below:

First,Last,Age
'John','Smith',28
'Mary', 'Smith',23
'Arthur','smith',55

remember ENTER means \\n.

To open the CSV file, we can use a library called csv.
csv has 2 different modes.  One converts the CSV file
into a list per line.  eg:

['John','Smith',28]
['Mary', 'Smith',23]
['Arthur','smith',55]

The other one creates dictionaries per line.  As per the below:

{'Name':'John','Last':'Smith','Age':28}
{'Name':'Mary','Last':'Smith','Age':23}
{'Name':'Arthur','Last':'Smith','Age':55}

Both methods require you to do a for loop to retrieve each member.
"""

raw_input(prompt)

import csv

csv_file =  'impatient_payments.csv'

with open(csv_file,'rb') as csv_file:
	impatient_data = csv.reader(csv_file,delimiter=",", quotechar='"')
	header = impatient_data.next()
	data = []
	for row in impatient_data:
		data.append(row)

prompt="""
The first method we utilize is called csv.reader.  It takes 3 arguments:
The name of the file, the delimiter and the quote character.  In CSV,
the delimiter is what separates values.  The quote character is the 
character, which indicates the value is a string. eg...

if delimiter = , then:

        "First Value", "Second Value" 

 	represents 2 values: "First Value" and "Second Value"

if delimiter = | then:

		"First Value"| "Second Value"

	represents 2 values: "First Value" and "Second Value"

		"First Value", "Second Value" 

	represents only 1 value now.

If quotechar = " then:

        "This is a string" 

    is a string.

If quotechar = $ then:

        $This is a string$

     is a string.

     	"This is a string"

     is no longer a string.

In the above example, we open the impatient_payments.csv file.
We then create a csv.reader object, which creates a list per row.
We remove the header, which tells us the column names.
We then append the rest of the rows (lists) to the data variable.

We can now print "data" to see the contents of the CSV file.

"""

raw_input(prompt)

prompt="""
We can print the header and data separately:
"""

raw_input(prompt)

prompt="""
HEADER: 
%s
"""

raw_input(prompt % header)

prompt="""
Press ENTER to see data:
"""

for row in data:
	print(row)

raw_input("Press ENTER to exit!")
