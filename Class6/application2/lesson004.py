import sqlite3

conn = sqlite3.connect('heartattack.db')
c = conn.cursor()

c.execute(""" SELECT * FROM heartattacks limit 10 """)

print "example rows:"
for row in c:
	print(row)

raw_input("Continue...")

c.execute(""" SELECT count(*) FROM heartattacks """)

count_records = c.fetchall()
print("records " + str(count_records[0][0]))

raw_input("Continue...")

c.execute(""" PRAGMA table_info('heartattacks') """)

columns=[]

for row in c:
	columns.append(str(row[1]))

print(columns)

raw_input("Continue...")

column_oriented={col:set() for col in columns}

c.execute(""" SELECT * FROM heartattacks """)

for row in c:
	for i in range(0,len(row)):
		append_col = columns[i]
		column_oriented[append_col].add(row[i])

print(column_oriented)

for col,lst in column_oriented.iteritems():
	print
	print(col)
	print(lst)
	print

c.close()


