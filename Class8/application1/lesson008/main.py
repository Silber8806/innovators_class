prompt="""
The previous lesson separated logic into different files.
Most likely, long term, packages would be a better option?

You might ask why?

Data sources tend to expand over time.  Connectivity between
these data sources very a lot.  You can have files and csvs, 
which require only a operating system call (to open).  You 
can have Excel or custom file formats, which require a 
special library (or api).  You might be dealing with the 
web/intranet, which requires knowledge of sockets or http requests. 
Finally, the number of databases expands on a yearly basis
to the point where the number of different retrieval protocols
is hard to predict.  The large eco-system means that we might
have 4-5 different data sources.  Each of these warrants it's 
own file (often enough).  It is therefore worth having 
a data directory, which is activated as a package.

Tests are another also worth treating as a package or at least
another directory (data doesn't have to be a package either). 
Tests tend to expand linearly or super-linearly with the 
functions/code in the production system.  Sooner or later, 
as software becomes segemented into smaller sub-systems, the 
tests themselves will start to mimic the divisions.  To prevent
single huge file syndrome, it's worth creating a directory of 
tests each focused on a specific aspect of the system (with
maybe a parent file that can run all tests at once).

Look at the code and notice how data and tests directories 
are created.  Note the __init__.py files and also the 
changes in the import statements in both main.py and 
medical_transactions.py
"""

raw_input(prompt)

import medical_transactions

medical_transactions.main() 

