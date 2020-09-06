#coding: utf-8

from flask import Flask, render_template, request

from .register import RegisterUser
from .login import LoginUser

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if ('' in (username, password)) == False:
           login = LoginUser()
           if login.login(username, password) == True:
               return "Vous êtes connecter"
           else:
               return "Veuillez vous créer un compte"
    else:
        return render_template("login.html")

@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        usermail = request.form["usermail"]
        password = request.form["password"]
        birthday = request.form["birthday"]
        if ('' in (username, usermail, password, birthday)) == False:
            register = RegisterUser()
            register.register(username, usermail, password, birthday)
            return "Vous avez été enregistré"
        else:
            return "Il y a eu un problème"
    else:
        return render_template("register.html")

@app.route('/about')
def about():
    return 'This is the about page'

@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404

#@app.errorhandler(DatabaseError)
#def special_exception_handler(error):
#    return 'Database connection failed', 500
