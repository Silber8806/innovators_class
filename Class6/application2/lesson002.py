import csv
import sqlite3

conn = sqlite3.connect('heartattack.db')

c = conn.cursor()

c.execute(""" drop table if exists heartattacks;""")

# Create table
c.execute(
			"""
			CREATE TABLE heartattacks
			(
				Year text,
				LocationAbbr text,
				LocationDesc text,
				GeographicLevel text,
				DataSource text,
				Class text,
				Topic text,
				Data_Value text,
				Data_Value_Unit text,
				Data_Value_Type text,
				Data_Value_Footnote_Symbol text,
				Data_Value_Footnote text,
				StratificationCategory1 text,
				Stratification1 text,
				StratificationCategory2 text,
				Stratification2 text,
				TopicID text,
				LocationID text,
				Location_1 text
			)
			"""
          )

with open('heartattacks.csv','rb') as f:
	reader = csv.reader(f)
	for row in reader:
		c.execute("INSERT INTO heartattacks VALUES (" + ",".join(['"' + col + '"' for col in row ]) + ")")

conn.commit()
conn.close()


