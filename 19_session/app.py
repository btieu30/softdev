'''
2 Whites & a Gray: Nada Hameed, Gitae Park, Brianna Tieu
Softdev
K19 -- Sessions Greetings
2022-11-07
'''

from flask import Flask, session, render_template, request, redirect, url_for

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_9#y2L"F4Q8z\n\xec]/'

temp_username = "brianna"
temp_password = "bt"

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('welcome'))
    else:
        return render_template( 'login.html' )

@app.route('/auth', methods=['GET', 'POST'])
def authenticate():
    if request.method == 'GET':
        if request.args['username'] == temp_username and request.args['password'] == temp_password:
            session['username'] = request.args['username']
            session['password'] = request.args['password']
            return redirect(url_for('welcome'))
        else: 
            if request.args['username'] != temp_username and request.args['password'] == temp_password:
                return render_template( 'login.html', login='incorrect username' )
            if request.args['username'] == temp_username and request.args['password'] != temp_password:
                return render_template( 'login.html', login='incorrect password' )
            if request.args['username'] != temp_username and request.args['password'] != temp_password:
                return render_template( 'login.html', login='incorrect username and password' )

@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    return render_template( 'response.html', user=session['username'] )

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.debug = True
    app.run()
