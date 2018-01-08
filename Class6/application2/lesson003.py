import sqlite3

conn = sqlite3.connect('heartattack.db')
c = conn.cursor()

c.execute(""" SELECT name, sql FROM sqlite_master WHERE type='table' """)

print "TABLES:"
for row in c:
	name, sql = row
	print(name)
	print(sql)

raw_input("Continue...")