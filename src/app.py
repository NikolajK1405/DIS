from flask import Flask, render_template, redirect, url_for, session, abort, request, flash
import psycopg2
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
import glob

app = Flask(__name__)

db = "dbname='***' user='***' host='***' password='***'"

conn = psycopg2.connect(db)
cur = conn.cursor()

bcrypt = Bcrypt(app)
     
@app.route('/',  methods=['POST', 'GET'])
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return 'du er logget ind!'


@app.route('/login', methods=['POST', 'GET'])
def login():
    username = request.form['username']
    password = request.form['password']

    find = " SELECT * from users where username = %s and password = %s "

    cur.execute(find, (username, password))

    LoggedIn = len(cur.fetchall()) != 0

    if LoggedIn:
        session['logged_in'] = True
        session['username'] = username
    else:
        flash('wrong password!')
    return redirect(url_for("home"))

@app.route('/cAccount', methods=['POST', 'GET'])
def cAccount():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        find = "select * from users where username = %s"
        cur.execute(find, (username,))
        unique = cur.fetchall()
        
        if len(unique) == 0:
            cur.execute("select * from users")
            count = len(cur.fetchall())
            insert = "INSERT INTO users(uid, username, password, kebabnum) VALUES (%s, %s, %s, %s)"
            cur.execute(insert, (count+1, username, password, 0))
            conn.commit()
            flash('Account creation succesful')
            return redirect(url_for("home"))
        else: 
            flash('Username already exists!')
    return render_template("cAccount.html")
        
        

#@app.route('/users')
#def user():
#    return render_template('user.html', users = users)

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True)
