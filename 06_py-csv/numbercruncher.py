'''
Um, Don't Know: May Qiu and Brianna Tieu
K06 : Divine your Destiny!

DISCO:
- We learned how to read a .csv file! (the process is similar to reading a .txt file)
- We learned Brianna and May are flops
- We use pop when removing from a list and append for adding to a list
- random.choices() allows us to have weighted probabilities

Q/C/C:
- When separating the csv files by row, why isn't the comma included in the array?
-print(random.choices(list(jobdict.keys()), weights = jobdict.values()))
 print(random.choices(joblist, cum_weights = perlist))
 What is the difference between the first and second line of code? The first line of code runs while the second does not. The error was "in choices total = cum_weights[-1] + 0.0   # convert to float
TypeError: can only concatenate str (not "float") to str

HOW THIS SCRIPT WORKS:
0: Read through the csv file
1: Append the first element in each row to a list of jobs and the second element in each row to a list of percentages.
2: Remove the first and last elements in lists (accounts for the "Job Class, Percentage" and "Total, 99.8" rows)
3: Create and populate new dictionary using our lists (keys are occupations, values are percentages)
4: Use random.choices() to have weighted probabilities
   random.choices() can take two lists (the first is a sequence we are choosing from, the second is the possibilities)
'''

import csv, random

joblist = []
perlist = []
jobdict = {}

with open('occupations.csv','r') as file:
    reader = csv.reader(file)
    #reads each line in the csv file and adds it to its respective list. The comma seperated the job and the percentage.
    for row in reader:
        joblist.append(row[0])
        perlist.append(row[1])

#popped off the job class percentage and the total, percentage
joblist.pop(0)
joblist.pop(len(joblist)-1)
perlist.pop(0)
perlist.pop(len(perlist)-1)

#populate the dictionary, with the key as the occupation and the value as the percentage (represented by a float value)
for x in range(len(joblist)):
    jobdict[joblist[x]] = float(perlist[x])

#randomly select an occupation from the keys of the dictionary, with the values/percentages as the weighted probabilities
print(random.choices(list(jobdict.keys()), weights = jobdict.values()))
