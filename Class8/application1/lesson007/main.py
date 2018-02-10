prompt="""
We have no separated all the previous logic into
files.  One file, database.py contains all the data
and data retrieval logic.

The medical_transactions.py contains all the logic 
for processing transactions and medical_procedures.

The test.py contains the create_test_json function.
Since, the function long term wil only be used 
to test teh functionality of the software, it is 
not worth keeping it with the main code.  

Tests are interesting conceptually.  When developing 
code, the larger the code base, the more likely changes
will cause bugs or unintended conseqences.

To solve this problem, we develop tests, which will
tell us if software is behaving as it previously was.

Software engineers dealing with large code bases will
have large suites of test functions, which will make 
sure everything was working as it previously was 
(and was intended to do)!

Navigate the contents of the directory to see how
the files are tied together.  Take extra notice 
of the import statements.

I would start at the medical_transactions.py file when
exploring this system.
"""

raw_input(prompt)

import medical_transactions

medical_transactions.main() 

