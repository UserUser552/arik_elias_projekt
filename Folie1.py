from flask import Flask

app = Flask(__name__)

@app.route("/") 
def hello_world():  
    return "Hello world" 

@app.route("/hello/<string:username>")
def hello_user(username):
    return "Hello <b>user</b> " + username
