import sqlite3
import csv

conn = sqlite3.connect('csvdata')

c = conn.cursor()

c.execute(
	'''
	CREATE TABLE users (id INTEGER PRIMARY KEY,
	name TEXT, email TEXT, country TEXT)
	'''
	)

c.execute(
	'''
	CREATE TABLE phone_numbers (id INTEGER PRIMARY KEY, 
	cellphone TEXT, homephone TEXT, workphone TEXT, 
	FOREIGN KEY (id) REFERENCES users(id))
	'''
	)

conn.commit()

conn.close()

print("users and phone_numbers tables created")

