from flask import Flask, redirect, url_for
from flask import render_template
from flask import request
import users

app = Flask(__name__)

colors = ["red", "green", "blue"]




@app.route("/", methods=["GET"])
def welcome():
    return render_template(
        "welcome_template.html",
        title = "Welcome"
        )
    


@app.route("/login", methods=["GET", "POST"])
def user_login():
    if request.method == "GET":
        return render_template(
        "login_template.html",
        title = "Login"
        )
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        
        users.User = users.User.from_db(username)
        return redirect(url_for("main"))


@app.route("/register", methods=["GET", "POST"])
def user_form():
    if request.method == "GET":
        return render_template(
        "template.html",
        title = "Kästchen Malen"
        )
    else:
        username = request.form.get("username")
        firstname = request.form.get("first_name")
        lastname = request.form.get("last_name")
        password = request.form.get("password")
        user = users.User(username, firstname, lastname, password)
        user.to_db()
        return f"Benutzer {username} wurde hinzugefügt"
    
@app.route("/main", methods=["GET"])
def main():
    new_colorindex = 0
    if "id" in request.args:
        id = request.args.get("id")
        colorindex = request.args.get("colorindex")
        new_colorindex = int(colorindex) + 1
        
    
    return render_template(
        "main_template.html",
        title = "Kästchen Malen",
        color = colors[new_colorindex],
        colorindex = new_colorindex
        )
    
  

        