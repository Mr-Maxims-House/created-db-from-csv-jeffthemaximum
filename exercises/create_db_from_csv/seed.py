import sqlite3
import csv

conn = sqlite3.connect('csvdata')

c = conn.cursor()

with open ('employees.csv') as csv_file:
	employees = csv.reader(csv_file, delimiter = ",")
	for row in employees:
		c.execute(
    """
    INSERT INTO users ("name", "email", "country") 
    VALUES (?, ?, ?);
    """,(row[0], row[4], row[5])
  )
		c.execute(
    """
    INSERT INTO phone_numbers ("cellphone", "homephone", "workphone") 
    VALUES (?, ?, ?);
    """,(row[1], row[2], row[3])
  )

print("Your database has been seeded")

conn.commit()
c.close()
		

