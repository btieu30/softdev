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

command = "create table student (name text, age int, id int);"
c.execute(command)

studentDict = {}
studentDict["name"] = []
studentDict["age"] = []
studentDict["id"] = []

# opening .csv file and reading it as a .DictReader object
# adding the job class and percentage to their appropriate slots in the dictionary
# .DictReader documentation --- https://docs.python.org/3/library/csv.html
with open('students.csv') as f:
    r =  csv.DictReader(f)
    for row in r:
        studentDict["name"].append(row['name'])
        studentDict["age"].append(row['age'])
        studentDict["id"].append(row['id'])
        things = row["name"] + row["age"] + row["id"]
        command = "insert into student values(things);"
        #command = "insert into student values ([studentDict["name"],studentDict["age"],studentDict["id"]])"
        #c.execute(command)
print(studentDict)

#insert = "INSERT INTO student (name, age, id) VALUES (?,?,?)",[studentDict["name"],studentDict["age"],studentDict["id"]]
select = "SELECT * FROM student"

#c.execute(insert)
rows = c.execute(select).fetchall()
for r in rows:
    print (r)


command = ""          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database
