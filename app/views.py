#coding: utf-8

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/login')
def login():
    return 'login page'

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/about')
def about():
    return 'This is the about page'
