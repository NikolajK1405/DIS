from flask import Flask, render_template, redirect, url_for, session, abort, request, flash
import psycopg2
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
import glob
from datetime import date
import re

from psycopg2.sql import NULL

app = Flask(__name__)

db = "dbname='nikolajkrarup' user='nikolajkrarup' host='localhost' password='Charlie04.'"

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
        username = None
        kebabnum = None
        if session.get('logged_in'):
            uid = session.get('uid')
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

    user = cur.fetchone()
    LoggedIn = len(user) != 0

    if LoggedIn:
        session['logged_in'] = True
        session['uid'] = (user[0])[0]
    else:
        flash('wrong password!')
    return redirect(url_for("start"))

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
        
        
@app.route('/post', methods = ['POST', 'GET'])
def post():
    if not session.get('logged_in'):
        return render_template('login.html')
    cur = conn.cursor()
    cur.execute("select kid, name from kebabsted order by name asc")
    kebabs = cur.fetchall()
    
    if request.method == 'POST':
        title = request.form['title']
        rating = request.form['rating']
        status = request.form['status']
        kid = request.form['kebab']
        
        try:
            rating = float(rating)
        except:
            flash("Rating must be a number")
            return render_template("post.html", kebabs = kebabs)
        if rating > 5 or rating < 1:
            flash("Rating must be a number between 1.0 and 5.0")
            return render_template("post.html", kebabs = kebabs)

        cur.execute("select * from posts")
        pid = len(cur.fetchall()) + 1
        uid = session.get('uid')
        
        update = "update users set kebabnum = kebabnum + 1 where uid = %s "
        cur.execute(update, (uid,)) 
        conn.commit()

        get = "select * from posts"
        d = date.today().strftime("%d/%m-%y")

        insert = "INSERT INTO posts(pid, title, rating, creator_id, kebab_id, date, status) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cur.execute(insert, (pid, title, rating, uid, kid, d, status))
        conn.commit()
        
        update = '''update kebabsted set rating = 
                                   (select avg(rating) from posts where kid = %s)
                                   where kid = %s '''
        cur.execute(update, (kid, kid)) 
        conn.commit()

        get = "select * from lokale where uid = %s"
        cur.execute(get, (uid,))
        lokale = cur.fetchone()
        lokale_id = lokale[1]
        if kid == lokale_id:
            visits = int(lokale[2])
            update = "update lokale set visits = %s where kid = %s"
            cur.execute(update, (visits+1, kid))
            conn.commit()

        return redirect(url_for("start"))

    else:
        return render_template("post.html", kebabs = kebabs)

@app.route('/feed', methods = ['GET'])
def feed():
    if not session.get('logged_in'):
        return render_template('login.html')
    cur = conn.cursor()
    find = '''select P.title, U.username, K.name, P.rating, P.status from Kebabsted K, posts P, users U
              where P.creator_id = U.uid and P.kebab_id = K.kid'''
    cur.execute(find)
    posts = cur.fetchall()
    return render_template('feed.html', posts = posts)
    
    
@app.route('/kebabPlaces', methods = ['POST', 'GET'])
def kebabPlaces():
    if not session.get('logged_in'):
        return render_template('login.html')
    cur = conn.cursor()
    find = "select * from Kebabsted"
    cur.execute(find)
    places = cur.fetchall()
    return render_template("kebabPlaces.html", places = places)

@app.route('/denLokale', methods = ['POST', 'GET'])
def denLokale():
    if not session.get('logged_in'):
        return render_template('login.html')
    uid = session.get('uid')
    cur.execute("select * from kebabsted order by name asc")
    kebabs = cur.fetchall()      

    if request.method == 'POST':
        t = request.form['type']
        newLokale = request.form['kebab']
        if t == "insert": 
            insert = "insert into lokale(uid, kid, visits) values (%s, %s, 0)"
            cur.execute(insert, (uid, newLokale))
            conn.commit()
        elif t == "update":
            update = "update lokale set kid = %s where uid = %s"
            cur.execute(update, (newLokale, uid))
            conn.commit()

    find = '''select K.name, K.rating, K.adresse, K.menu, L.visits from Kebabsted K, lokale L 
                                              where L.uid = %s and L.kid = K.kid'''
    cur.execute(find, (uid,))
    lokale = cur.fetchone()
    if lokale == None:
        msg = "You haven't picked a Lokal"
        return render_template("lokale.html", lokale = msg, kebabs = kebabs)
    else:
        return render_template("lokale.html", lokale = lokale, kebabs = kebabs)
        

#@app.route('/users')
#def user():
#    return render_template('user.html', users = users)

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True)
