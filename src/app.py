from flask import Flask, render_template, redirect, url_for, session, abort, request, flash
import requests
from bs4 import BeautifulSoup
import psycopg2
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
import glob
import pandas as pd
import random

app = Flask(__name__)

db = "dbname='nikolajkrarup' user='nikolajkrarup' host='localhost' password='Charlie04.'"

conn = psycopg2.connect(db)
cursor = conn.cursor()

bcrypt = Bcrypt(app)
     
@app.route('/',  methods=['POST', 'GET'])
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return 'du er logget ind!'


@app.route('/login', methods=['POST'])
def login():
    cur = conn.cursor()
    username = request.form['username']
    password = request.form['password']

    insys = f''' SELECT * from users where username = '{username}' and password = '{password}' '''

    cur.execute(insys)

    ifcool = len(cur.fetchall()) != 0

    if ifcool:
        session['logged_in'] = True
        session['username'] = username
    else:
        flash('wrong password!')
    return redirect(url_for("home"))


#@app.route('/users')
#def user():
#    return render_template('user.html', users = users)

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True)
