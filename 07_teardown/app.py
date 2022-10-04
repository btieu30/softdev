'''
Git Bri in May: Gitae Park, May Qiu, Brianna Tieu
SOFTDEV
pd07
2022-10-03
time spent: .5 hr
'''

from flask import Flask

app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"  # Q4: Will this appear anywhere? How u know?

app.run()  # Q5: Where have you seen similar constructs in other languages?


'''
DISCO:
- You have to click on the link printed in the console to open the webpage.
- All machines that successfully run the code above must have flask installed.

QCC:
0. Creating an object in Java
1. file paths, URLs
2. It prints in the console.
3. __main__
4. This appears on the local webpage. We saw "No hablo queso" on the webpage
   that appears when you click the link provided in the terminal after running
   app.py.
5. java
...

INVESTIGATIVE APPROACH:
- Our team realized that we needed to click the link in order to generate
output in our console. We also installed flask on our local/home machines in
order to run the code.
'''
