from flask import Flask, render_template, request

app = Flask(__name__)

users = [
    {'UID': '01',
     'name': 'VT'},
    {'UID': '02',
     'name': 'Sion'},
    {'UID': '03',
     'name': 'Niko'}
    ]
     

@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return f"Received: {username}, {password}"
    return render_template('login.html')

@app.route('/users')
def user():
    return render_template('user.html', users = users)

if __name__ == '__main__':
    app.run(debug=True)

