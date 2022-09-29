'''
Git Bri in May: Gitae Park, Brianna Tieu, May Qiu
SoftDev
K04 -- krewes/Making a random generator to return the name of a student from any class using dictionaries
2022-09-23
.3 hrs
OP Summary for randomdevo()
1) Create list of the keys in krewes
2) Choose a random key / period in the list
3) Create list of the devos in the selected key / period
4) Choose a random devo in the period
5) Print the selected devo's name and period
OP Summary for morethanone()
1) Create variable numberofdevos to take user input
2) Check if numberofdevos is within range (1 < numberofdevos < 106)
   If so, proceed.
   Else, user selects new numbers until there is one in range.
3) Create for loop that continues until the required number of devos are printed.
   Inside the for loop: ( steps a-e are the same as randomdevo() )
   a) Create list of the keys in krewes
   b) Choose a random key / period in the list
   c) Create list of the devos in the selected key / period
   d) Choose a random devo in the period
   e) Print the selected devo's name and period
   f) Check if the list of devos is of length 1
      If so, remove key / period from krewes
      Else, continue in the loop
Q/C/C
What other things can dictionaries do?
What other random methods are there and how do we utilize it?
How would we import all the names of everyone from Github?
DISCO
We needed to cast the .keys into a list otherwise we got the Type Error: "dict_keys" object is not subscriptable
'''
import random
krewes = {
           2:["NICHOLAS",  "ANTHONY",  "BRIAN",  "SAMUEL",  "JULIA",  "YUSHA",  "CORINA",  "CRAIG",  "FANG MIN",  "JEFF",  "KONSTANTIN",  "AARON",  "VIVIAN",  "AYMAN",  "TALIA",  "FAIZA",  "ZIYING",  "YUK KWAN",  "DANIEL",  "WEICHEN",  "MAYA",  "ELIZABETH",  "ANDREW",  "VANSH",  "JONATHAN",  "ABID",  "WILLIAM",  "HUI",  "ANSON",  "KEVIN",  "DANIEL",  "IVAN",  "JASMINE",  "JEFFREY", "Ruiwen"],
           7:["DIANA",  "DAVID",  "SAM",  "PRATTAY",  "ANNA",  "JING YI",  "ADEN",  "EMERSON",  "RUSSELL",  "JACOB",  "WILLIAM",  "NADA",  "SAMANTHA",  "IAN",  "MARC",  "ANJINI",  "JEREMY",  "LAUREN",  "KEVIN",  "RAVINDRA",  "SADI",  "EMILY",  "GITAE",  "MAY",  "MAHIR",  "VIVIAN",  "GABRIEL",  "BRIANNA",  "JUN HONG",  "JOSEPH",  "MATTHEW",  "JAMES",  "THOMAS",  "NICOLE",  "Karen"],
           8:["ALEKSANDRA",  "NAKIB",  "AMEER",  "HENRY",  "DONALD",  "YAT LONG",  "SEBASTIAN",  "DAVID",  "YUKI",  "SHAFIUL",  "DANIEL",  "SELENA",  "JOSEPH",  "SHINJI",  "RYAN",  "APRIL",  "ERICA",  "JIAN HONG",  "VERIT",  "JOSHUA",  "WILSON",  "AAHAN",  "GORDON",  "JUSTIN",  "MAYA",  "FAIYAZ",  "SHREYA",  "ERIC",  "JEFFERY",  "BRIAN",  "KEVIN",  "SAMSON",  "BRIAN",  "HARRY",  "Wanying", "Kevin"]
         }
def randomdevo():
    period = list(krewes.keys())
    randp = random.choice(period)
    devos = list(krewes.get(randp))
    randd = random.choice(devos)
    print(str(randd) + " from period " + str(randp))


def morethanone():
    numberofdevos = int(input("How many devos would you like to summon? Pick a number between 1-106.\n"))
    while numberofdevos > 106 or numberofdevos < 1:
        print("You are dumb. Read directions.")
        numberofdevos = int(input("How many people would you like? Pick carefully\n"))
    for x in range(numberofdevos):
        period = list(krewes.keys())
        randp = random.choice(period)
        devos = list(krewes.get(randp))
        randd = random.choice(devos)
        print(str(randd) + " from period " + str(randp))
        krewes[randp].remove(randd)
        if len(devos) == 1:
            krewes.pop(randp)




#randomdevo()
morethanone()
