'''
Um, I Don't Know: Brianna Tieu, May Qiu
SoftDev
K05 -- krewes/Making a random generator to return the name of a student from any class using dictionaries
2022-09-29
.5 hrs
OP Summary for krewes.py
1) Read through krewes.txt
2) Initialize three dictionaries (one / period)
3) Split krewes by "@@@"
4) Create variables to get the devo's period, name and ducky name
5) Sort devos by period, using their name as the key and the ducky name as the value
6) Generate random int from 1-3, each corresponding to a period of sawftdev
7) Create and randomly select from a list of the selected period's keys
8) Get the value of the corresponding key
9) Print out all the devo's info

Q/C/C
What other things can dictionaries do?
What other random methods are there and how do we utilize it?
DISCO
We can use indices right after the .split() method to refer to elements in the newly created list.
'''
import random

#reading and opening the text file
krewes_file = open("krewes.txt", "r")
text = krewes_file.read()

#creating separate dictionaries for all three periods
second = {}
seventh = {}
eighth = {}

#split data by '@@@', as info for each devo is separated by '@@@'
data = text.split("@@@")

#for each devo, the order of the info is period, devo name, ducky name
for x in data:
    period = x.split("$$$")[0]
    name = x.split("$$$")[1]
    ducky = x.split("$$$")[2]

    #intialize the new dict key and recognize the devo by period first,
    #then append the devo and ducky name
    if period == "2":
        second[name] = ducky
    if period == "7":
        seventh[name] = ducky
    if period == "8":
        eighth[name] = ducky

#generate random ints, ranging from 1-3 to randomly select the period
randp = random.randint(1,3)
if randp == 1:
    print("Period: 2")
    randd = random.choice(list(second.keys())) #randomly select a devo
    print("Devo Name: " + str(randd))
    print("Ducky Name: " + str(second.get(randd))) #get the value paired with the random devo's first name (which is their ducky name)
if randp == 2:
    print("Period: 7")
    randd = random.choice(list(seventh.keys()))
    print("Devo Name: " + str(randd))
    print("Ducky Name: " + str(seventh.get(randd)))
if randp == 3:
    print("Period: 8")
    randd = random.choice(list(eighth.keys()))
    print("Devo Name: " + str(randd))
    print("Ducky Name: " + str(eighth.get(randd)))
