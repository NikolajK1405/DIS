from flask import Flask, render_template, redirect, url_for, session, abort, request, flash
import psycopg2
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
import glob
from datetime import date

app = Flask(__name__)

db = "dbname='nikolajkrarup' user='nikolajkrarup' host='localhost' password='Charlie04.'"

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
    user_row = cur.fetchone()
    LoggedIn = len(user_row) != 0

    if LoggedIn:
        session['logged_in'] = True
        session['username'] = username
        session['uid'] =user_row[0]
    else:
        flash('wrong password!')
    return redirect(url_for("home"))

@app.route('/cAccount', methods=['POST', 'GET'])
def cAccount():
    cur = conn.cursor()
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
        
        
@app.route('/post', methods = ['POST', 'GET'])
def post():
    cur = conn.cursor()
    if request.method == 'POST':
        title = request.form['title']
        rating = request.form['rating']
        status = request.form['status']
        
        cur.execute("select * from posts")
        pid = len(cur.fetchall()) + 1
        uid = session.get('uid')
        kid = 1 # implement propper kebab selection
        
        get = "select * from posts"
        d = date.today().strftime("%d/%m-%y")

        insert = "INSERT INTO posts(pid, title, rating, creator_id, kebab_id, date, status) VALUES (%s, %s, %s, %s, %s, %s, %s)"

        cur.execute(insert, (pid, title, rating, uid, kid, d, status))
        conn.commit()
        return redirect(url_for("home"))
    return render_template("post.html")

#@app.route('/users')
#def user():
#    return render_template('user.html', users = users)

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True)
