# 2 Whites & a Gray: Brianna Tieu, Nada Hameed, Gitae Park
### SoftDev
### K17 -- Shell Game
### 2022-10-25
### time spent: .6 hr

## how-to :: SQLITE
* To activate SQLITE from your terminal: ```sqlite3;```
* To either access an existing database or to create a new one in SQLITE, type ```sqlite3 nameOfDB;```
* To create tables: ```create table tableName (colName0, datatype0, colName1, datatype1 ...);```
* To Insert table values: ```insert into tableName values(val0, val1, ...);```
* To see your tables returned within the terminal: ```select * from tableName```
* Semicolons in SQLITE are essential after every line
* To save your work in the database, you can use ```.save nameofDB.db```
    * Keep in mind that the .save command overwrites any preexisting files with the same name once it is run. 
* ```.databases``` allows you to see the path of your database in the terminal
* To TERMINATE SQLITE in your terminal, use Ctrl+D