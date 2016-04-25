import sqlite3
import csv
conn = sqlite3.connect('csvdata.db')

c = conn.cursor()

c.execute(
	'''
	CREATE TABLE users (id INTEGER PRIMARY KEY,
	name TEXT, email TEXT, country TEXT)
	'''
	)

c.execute(
	'''
	CREATE TABLE phone_numbers (cellphone TEXT, homephone TEXT, 
	workphone TEXT, FOREIGN KEY (name_id) REFERENCES users(id))
	'''
	)

c.commit()

