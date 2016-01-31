# Relational DB and Foreign Keys

### Learning Objectives
***Students will be able to...***

* Diagram out an ERD of a Relational Database (Review)
* Use Foreign Keys to connect multiple tables in SQLite
* Build a database with a one to one relationship
* Build a database with a one to many relationship
* Query a database
* Make a Join Table SQL query (Luxury Goal)

---

### Context

* We've done CRUD with a single table database. That's all great but as our data becomes bigger we are going to need more tables for organization.

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
* We'll be using the ERD diagram website: [http://ondras.zarovi.cz/sql/demo/](http://ondras.zarovi.cz/sql/demo/)

***Hints***

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
INSERT INTO gyms (name, city, rate) VALUES ('Golds Gym', 'Los Angeles', 40), ('Equinox', 'New York', 150), ('Planet Fitness', 'New Jersey', 15);
```
* Lets make sure we got everything right

```
SELECT * FROM gyms;
```
* Add the following members

```
INSERT INTO members (gym_id, first_name, last_name, age) VALUES (1, 'Arnold', 'Schwarzenegger', 100), (2, "Jason", "Ng", 27), (2, "Robert", "Swallow", 21), (2, "Jeff", "Maxim", 31), (3, "Luke", "Skywalker", 89);
```
* Lets make sure we got everything right here

```
SELECT * FROM members;
```
* Now let's use the foreign key to grab us some items

```
SELECT members.first_name FROM members, gyms WHERE members.gym_id=2;
```

***Challenge Question***
* Let's say we're at the point in our Python code where we've got the name of a gym stored in a variable, like below:
```
name = 'Equinox'
```
* And from here, I want to find the members who belong to that Gym.
* I would probably do a two step process. **First**, I would query gyms to find the ID of the gym:
```
gym_id = "SELECT id FROM gyms WHERE name = 'Equinox';"
```
* And based on our example database, `gym_id = 2 ` at this point.
* **Second**, I would query the members table, and find all members who have `2` in their `gym_id` column, as shown below:
```
members_of_gym = "SELECT * FROM members WHERE gym_id=gym_id;"
```
* And this would return to me all members who belong to the gym called `Equiniox`. 
* My problem with this is that it's two steps. **First** we query the gym table, and **second** we query the members table. Is there a way to do this in one step? All I could think of was this:
```
members_of_gym = SELECT * FROM members WHERE gym_id=(SELECT id FROM gyms WHERE name = 'Equinox');
```
* **Spoiler alert! Solution below!**

* The **solution** is to use an `AND` SQL statement:
```
members_of_gym = '''
  SELECT *
  FROM member, gyms
  WHERE members.gym_id=gyms.id AND gyms.name='Equinox';
'''
```
