#2 Whites & a Gray: Nada Hameed, Gitae Park, Brianna Tieu
#SoftDev  
#K18: (Python+SQLite)3: A Mare Widge Made in Hebben
#Oct 2022

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O

#MAKE SURE TO REMOVE ANY EXISTING DATABASES THAT ARE CREATED THROUGH db_builder.py TO AVOID ERROR MESSAGES
# - run "rm students.db" every time after you "python db_builder.py"

DB_FILE="students.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================


c.execute("CREATE TABLE student (name TEXT, age INTEGER, id INTEGER)")

f = open('students.csv')
contents = csv.reader(f)

insert = "INSERT INTO student (name, age, id) VALUES (?,?,?)"

c.executemany(insert, contents)
select = "SELECT * FROM student"

rows = c.execute(select).fetchall()
for r in rows:
    print (r)


command = ""          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database


