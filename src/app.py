from flask import Flask, render_template, redirect, url_for, session, abort, request, flash
import psycopg2
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
import glob
import re

from psycopg2.sql import NULL

app = Flask(__name__)

db = "dbname='test' user='postgres' host='localhost' password='emil494k'"

conn = psycopg2.connect(db)
cur = conn.cursor()

bcrypt = Bcrypt(app)

# Passwords must contain the word kebab, an uppercase letter, and no special chars
re_password = r'(?=.*(kebab|Kebab).*)(?=.*[A-Z].*)[a-zA-Z0-9]*'

@app.route('/',  methods=['POST', 'GET'])
def start():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return redirect(url_for("home"))

@app.route('/home',  methods=['POST', 'GET'])
def home():
    username = None
    kebabnum = None
    if session.get('logged_in'):
        uid = session.get('uid')[0]
        find = " SELECT username, kebabnum from users where uid = %s"
        cur.execute(find, (uid,))
        user = cur.fetchone()
        username = user[0]
        kebabnum = user[1]
    return render_template("home.html", username=username, kebabnum = kebabnum)


@app.route('/login', methods=['POST', 'GET'])
def login():
    username = request.form['username']
    password = request.form['password']

    find = " SELECT * from users where username = %s and password = %s "

    cur.execute(find, (username, password))

    user = cur.fetchall()
    LoggedIn = len(user) != 0

    if LoggedIn:
        session['logged_in'] = True
        session['uid'] = user[0]
    else:
        flash('wrong password!')
    return redirect(url_for("start"))

@app.route('/cAccount', methods=['POST', 'GET'])
def cAccount():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']        

        find = "select * from users where username = %s"
        cur.execute(find, (username,))
        unique = cur.fetchall()        

        if len(unique) == 0:
            if not re.match(re_password, password):
                flash('''Invalid password, your password must contain an upper case letter and the word kebab. 
                      No special characters are allowed''')
                return redirect(url_for("cAccount"))
            cur.execute("select * from users")
            count = len(cur.fetchall())
            insert = "INSERT INTO users(uid, username, password, kebabnum) VALUES (%s, %s, %s, %s)"
            cur.execute(insert, (count+1, username, password, 0))
            conn.commit()
            flash('Account creation succesful')
            return redirect(url_for("start"))
        else: 
            flash('Username already exists!')
    return render_template("cAccount.html")
        
@app.route('/kebabPlaces', methods=['POST', 'GET'])
def kebabPlaces():
    find = "select * from Kebabsted"
    cur.execute(find)
    places = cur.fetchall()
    print(places)
    return render_template("kebabPlaces.html", places = places)

#@app.route('/users')
#def user():
#    return render_template('user.html', users = users)

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True)
