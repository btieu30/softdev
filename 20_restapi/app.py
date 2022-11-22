'''
BLT: Brianna Tieu and Lauren Lee
SoftDev pd07
K20 - A RESTful Journey Skyward
2022-11-21
time spent: .5 hr
'''
# importing required libs (notes and code, resources under python3)
from flask import Flask, render_template
from urllib import request
import json

app = Flask (__name__)

# get the key as a string
key = ""
with open("key_nasa.txt", "r") as file:
    key = file.read()

@app.route("/")
def display():
    url = f"https://api.nasa.gov/planetary/apod?api_key={key}" # f string to append the required key
    disp = request.urlopen(url) # open the url, which is now a complete string with the required key
    #print(disp)
    dict = json.loads(disp.read()) # create python dict to store the JSON data presented on the NASA site
    
    return render_template('main.html', picture=dict['url'], explanation=dict['explanation']) # return the template and replace the required fields (picture's url and picture's explanation)
if __name__ == "__main__":
    app.debug = True
    app.run()
