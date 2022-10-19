from flask import Flask, render_template
app = Flask(__name__)    #create Flask object

@app.route("/")
def webpage():
    return render_template('index.html')

if __name__ == "__main__": #false if this file imported as module
#enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
