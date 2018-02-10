prompt="""
Honestly, code and data sources should be separate.
The fact that database.py contained JSON objects as
strings is rather worrisome.

Instead, we should take each of the json objects and 
store them as separate files.  Why?

First, data that exists in file is not modified after
the code execution.  It will go back to the state 
represented in the code.  This is one reason why 
we tend to separate code from data.  

Some people might argue that you could write a python 
procedure that dynamically modifies the objects in
the python file.  It's a horrible idea in this case,
it just makes life a lot more complicated (your 
basically creating a mini-language for JSON processing).
It's not worth it.

Second, other programs might want to access the data 
itself.  by isolating the data into separate files, 
multiple programs can read and modify the files at the 
same time.  This allows the computers to see the state
of: procedures, providers, patients and insurance companies
at any time.  

Note, the beauty of file objects is that
they provide a simple API for reading, writing and appending
data to files.

Look at the data directory and notice how I separate the
json objects in database.py into separate json objects:
patient.json, insurance.json, procedure.json and provider.json.
"""

raw_input(prompt)

import medical_transactions

medical_transactions.main() 

