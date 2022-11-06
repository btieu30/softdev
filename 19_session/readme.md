# 2 Whites & a Gray: Nada Hameed, Gitae Park, Brianna Tieu
## Softdev
## K19 -- Sessions Greetings
## 2022-11-07

### DISCO:
- We must import request, redirect and url_for in order to use it.
- ```redirect(url_for())``` expects a function, not an app route as a param. 
- ```session['username'] = request.args['username']``` creates a cookie for us that keeps the user logged in even when the Flask server is taken offline.
- A user's session only actually terminates once the user clicks the log out, which removes any (locally) stored cookies. 

### QCC:
- What does creating app.secret_key do for us?