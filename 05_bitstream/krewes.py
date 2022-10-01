'''
Um, I Don't Know: Brianna Tieu, May Qiu
SoftDev
K05 -- krewes/Making a random generator to return the name of a student from any class using dictionaries
2022-09-29
1 hr
OP Summary for krewes.py
1) Read through krewes.txt
2) Initialize krewes dictionary
3) Split .txt file by "@@@"
4) Separate the devo's period and the devo + ducky name
5) Populate krewes
    a) check if the devo's period has already been created as a key to
       prevent overwriting data
    b) if it already exists, append the devo info to the list
6) Randomly choose a key / period
7) In the key, randomly choose a devo and print all the devo's information

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

#create an empty dictionary, to be filled with all the devos
krewes = {}

#split data by "@@@", as info for each devo is separated by "@@@"
data = text.split("@@@")
#for each devo, the order of the info is period, devo name, ducky name
for devo in data:
    x = devo.split("$$$")
    #the value of each key is a list of lists :o, each list having a devo name and ducky name
    info = x[1:]
    #check if the key already exists, so that values are not overwritten
    if x[0] in krewes.keys():
        krewes[x[0]].append(info)
    else:
        krewes[x[0]] = [info]

#randomly select a period
period = random.choice(list(krewes.keys()))

#within the period, randomly select a list of one devo's info
devo_info = random.choice(krewes[period])

#put it all together and print! (the first item in devo_info is the devo's name, the second is the ducky's name)
print("Devo " + str(devo_info[0]) + " with ducky " + str(devo_info[1]) + " from Period " + str(period))  

#print(krewes)