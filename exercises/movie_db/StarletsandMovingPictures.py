import sqlite3

db = sqlite3.connect('movie')

cursor = db.cursor()

cursor.execute('''
  CREATE TABLE actors(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    movie_title TEXT
  );
''')

cursor.execute('''
  CREATE TABLE actors(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT
    FOREIGN KEY(gym_id) REFERENCES movie(id)
  );
''')


db.commit()
# db.close()

print("Starlets and Moving Pictures")

MOVIES = [
  [1,"Iron Man"],
  [2,"Iron Man 2"],
  [3,"Iron Man 3"],
  [4,"Captain America"],
  [5,"Captain America 2"]
  [6,"Captain America 3"]
  [7,"The Incredible Hulk"]
  [8,"Thor"]
  [9,"Thor 2"]
  [10,"Avengers"]
  [11,"Avengers 2"]
]

ACTORS = [
  [1, "Robert", "Downey Jr"],
  [2, "Terrence", "Howard"],
  [3, "Gwyneth", "Paltrow"],
  [4, "Jeff", "Bridges"],
  [5, "Don", "Cheadle"],
  [6, "Scarlett", "Johansson"],
  [7, "Chris", "Evans"],
  [8, "Anthony", "Mackie"],
  [9, "Jeremy", "Renner"],
  [10, "Edward", "Norton"]
  [11, "Liv", "Tyler"]
  [12, "Tim", "Roth"]
  [13, "William", "Hurt"
  [14, "Natalie", "Portman"]
  [15, "Tom", Hiddleson"]
  [16, "Mark", "Ruffalo"]
]

for movies in MOVIES:
  cursor.execute(
    """
    INSERT INTO movies ("title") 
    VALUES (?);
    """,(movies[1], movies [2], movies [3], movies [4], movies [5], movies [6], movies [7], movies [8], movies [9], movies [10], movies [11] )
  )

db.commit()

for actor in ACTORS:
  cursor.execute(
    """
    INSERT INTO movies ("movies_id", "first_name", "last_name")
    VALUES (?, ?, ?);
    """, (actor[0], actor[1], actor[2], actor[3], actor[4], actor[5], actor[6], actor[7], actor[8], actor[9], actor[10], actor[11])
  )

db.commit()
cursor.close()
