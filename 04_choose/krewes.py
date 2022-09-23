'''
Git Bri in May: Gitae Park, Brianna Tieu, May Qiu
SoftDev
K04 -- krewes/Making a random generator to return the name of a student from any class using dictionaries
2022-09-22
.3 hrs
'''
import random
def randomdevo():
    krewes = { 2: ["Loser Fang", "Brian Chen", "Aaron Gershkovich", "Ayman Habib", "Andrew Piatetsky"], 7: ["May", "Bri", "Gitae","Ravindra","Kevin Liu", "GT", "Karen"], 8: ["Jeff", "bd", "cd"]}
    period = list(krewes.keys())
    lenp = len(period)
    randp = random.randint(0,lenp-1)
    devos = list(krewes.get(period[randp]))
    lend = len(devos)
    randd = random.randint(0,lend-1)
    print(devos[randd])

randomdevo()
