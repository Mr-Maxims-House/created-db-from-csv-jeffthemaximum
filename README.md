# Relational DB and Foreign Keys

### Learning Objectives
***Students will be able to...***

* Diagram out an ERD of a Relational Database (Review)
* Use Foreign Keys to connect multiple tables in SQLite
* Build a database with a one to one relationship
* Build a database with a one to many relationship
* Make a Join Table SQL query (Luxury Goal)

---

### Context

* We've done CRUD with a single table database. That's all great but as our data becomes bigger we are going to need more tables for organization. This is where the relationships come in.

---

### Lessons

##### Part 1 - ERDs / Relationships Review

* What are some examples of a one to one relationship? How about a one to many relationship?
	* One to One
		* A person has one SSN
		* A person has one passport
	* One to Many
		* A person has one birthday / A birthday has many people
		* A person has one gym / A gym has many members
		* A pet has one owner / A person has many pets

***One to One***

* A row in a table has a relationship with another row in another table. 
* This relationship works both ways between the two tables. Each row can have a connection only with one other row from another table. 

***One to Many***

* A row in one table can have a connection with multiple rows in another table
* In reverse, multiple rows in a table can be connected to the same row in another table

***Five Min Exercise***

* Take the examples above and draw out an ERD of them. 
* We'll be using the ERD diagram website: (put website here)

***Notes***

* Which table takes precedent over the other in a relational database?
* Is there a parent table and a child table?

	
##### Part 2 - SQL Foriegn Keys

* Foreign Keys allow us to reference one table to another.
* They are an extra `column` in a table and are entered into the child table to reference it's parent

***Example Code Along***

* Let's build out the gym example above
* We'll have two tables
* Only one table will have a `Foreign Key` column

```
CREATE TABLE gyms (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT,
  city TEXT,
  rate INTEGER
);

CREATE TABLE members(
  member_id INTEGER PRIMARY KEY AUTOINCREMENT,
  gym_id INTEGER,
  first_name TEXT,
  last_name TEXT,
  age INTEGER,
  FOREIGN KEY(gym_id) REFERENCES gyms(id)
);
```
* Add the following gyms

```
INSERT INTO gyms (name, city, rate) VALUES ('Golds Gym', 'Los Angelos', 40), ('Equinox', 'New York', 150), ('Planet Fitness', 'New Jersey', 15);
```
* Lets make sure we got everything right

```
SELECT * FROM garages;
```
* Add the following members

```
INSERT INTO members (gym_id, first_name, last_name, age) VALUES (1, 'Arnold', 'Schwarzenegger', 100), (2, "Jason", "Ng", 27), (2, "Robert", "Swallow", 21), (2, "Brian", "McHugh", 21), (3, "Luke", "Skywalker", 89);
```
* Lets make sure we got everything right here

```
SELECT * FROM members;
```
* Now let's use the foreign key to grab us some items

```
SELECT members.first_name FROM members, gyms WHERE members.gym_id=2;
```


