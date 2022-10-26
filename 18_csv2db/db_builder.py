#2 Whites & a Gray: Nada Hameed, Gitae Park, Brianna Tieu
#SoftDev  
#skeleton/stub :: SQLITE3 BASICS
#Oct 2022

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


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


