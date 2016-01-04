import sqlite3

db = sqlite3.connect('fitness')

cursor = db.cursor()

cursor.execute('''
  CREATE TABLE gyms (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    city TEXT,
    rate INTEGER
  );
''')

cursor.execute('''
  CREATE TABLE members(
    member_id INTEGER PRIMARY KEY AUTOINCREMENT,
    gym_id INTEGER,
    first_name TEXT,
    last_name TEXT,
    age INTEGER,
    FOREIGN KEY(gym_id) REFERENCES gyms(id)
  );
''')

db.commit()
db.close()