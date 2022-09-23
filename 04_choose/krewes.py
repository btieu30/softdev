'''
Git Bri in May: Gitae Park, Brianna Tieu, May Qiu
SoftDev
K04 -- krewes/Making a random generator to return the name of a student from any class using dictionaries
2022-09-23
.3 hrs

OP Summary
We decided to divide the random portion into two parts.
We first wanted to randomly choose a key and then after we did so, we choose a devo from that key.
So, we created a list of those keys by using the .keys method and by turning it into a list.
We then used random.randint in order to choose a random index in that list.
After choosing a random key, we redid our steps to find a random devo within that period.

Q/C/C
What other things can dictionaries do?
What other random methods are there and how do we utilize it?
How would we import all the names of everyone from Github?

DISCO
We needed to cast the .keys into a list otherwise we got the Type Error: "dict_keys" object is not subscriptable
'''
import random
def randomdevo():
    krewes = {
           2:["NICHOLAS",  "ANTHONY",  "BRIAN",  "SAMUEL",  "JULIA",  "YUSHA",  "CORINA",  "CRAIG",  "FANG MIN",  "JEFF",  "KONSTANTIN",  "AARON",  "VIVIAN",  "AYMAN",  "TALIA",  "FAIZA",  "ZIYING",  "YUK KWAN",  "DANIEL",  "WEICHEN",  "MAYA",  "ELIZABETH",  "ANDREW",  "VANSH",  "JONATHAN",  "ABID",  "WILLIAM",  "HUI",  "ANSON",  "KEVIN",  "DANIEL",  "IVAN",  "JASMINE",  "JEFFREY", "Ruiwen"], 
           7:["DIANA",  "DAVID",  "SAM",  "PRATTAY",  "ANNA",  "JING YI",  "ADEN",  "EMERSON",  "RUSSELL",  "JACOB",  "WILLIAM",  "NADA",  "SAMANTHA",  "IAN",  "MARC",  "ANJINI",  "JEREMY",  "LAUREN",  "KEVIN",  "RAVINDRA",  "SADI",  "EMILY",  "GITAE",  "MAY",  "MAHIR",  "VIVIAN",  "GABRIEL",  "BRIANNA",  "JUN HONG",  "JOSEPH",  "MATTHEW",  "JAMES",  "THOMAS",  "NICOLE",  "Karen"],
           8:["ALEKSANDRA",  "NAKIB",  "AMEER",  "HENRY",  "DONALD",  "YAT LONG",  "SEBASTIAN",  "DAVID",  "YUKI",  "SHAFIUL",  "DANIEL",  "SELENA",  "JOSEPH",  "SHINJI",  "RYAN",  "APRIL",  "ERICA",  "JIAN HONG",  "VERIT",  "JOSHUA",  "WILSON",  "AAHAN",  "GORDON",  "JUSTIN",  "MAYA",  "FAIYAZ",  "SHREYA",  "ERIC",  "JEFFERY",  "BRIAN",  "KEVIN",  "SAMSON",  "BRIAN",  "HARRY",  "Wanying", "Kevin"]
         }

    period = list(krewes.keys())
    lenp = len(period)
    randp = random.randint(0,lenp-1)
    devos = list(krewes.get(period[randp]))
    lend = len(devos)
    randd = random.randint(0,lend-1)
    print(devos[randd] + " from period " + str(period[randp]))

randomdevo()
