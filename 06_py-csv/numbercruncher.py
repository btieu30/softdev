'''
Um, Don't Know: May Qiu and Brianna Tieu
K06 : Divine your Destiny!

DISCO:
- We learned how to read a .csv file! (the process is similar to reading a .txt file)
- We learned Brianna and May are flops
- um

Q/C/C:
- When separating the csv files by row, why isn't the comma included in the array?
-  

'''

import csv
from random import choice


with open('occupations.csv','r') as file:
    reader = csv.reader(file)
    for row in reader:
        job = row[0]
        per = row[1]


        