import sys
import gzip
import os.path

prompt = """
Data takes up a lot of space!

Some of these files are 50 megabytes!

This procedure unzips the gzip compressed
data files!  Converting them from a 
space efficient format to one that 
is easier to work with!

type yes to uncompress files!

Required for other lessons to work!
"""

answer = ""
files = ['death.data.gz','impatient_payments.csv.gz','heartattacks.csv.gz','heartattacks.db.gz']
raw_input(prompt)

while (answer.lower() not in ("yes","y","exit")):
	answer=raw_input("Do you want to uncompress files? (y/yes/Y/Yes)")

if (answer.lower() in ("yes","y")):
	for file in files:
		if os.path.isfile(file):	
			with gzip.open(file, 'rb') as f:
				print("converting: %s to %s" % (file,file.replace(".gz","")))
				file_contents = f.read()
				open(file.replace('.gz',''),'w').write(file_contents)
	sys.exit(0)
else:
	sys.exit(0)