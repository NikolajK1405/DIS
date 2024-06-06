from flask import Flask, render_template

app = Flask(__name__)

users = [
    {'UID': '01',
     'name': 'VT'},
    {'UID': '02',
     'name': 'Sion'},
    {'UID': '03',
     'name': 'Niko'}
    ]
     

@app.route('/')
def hello():
    return 'DIKUs største baller!'

@app.route('/users')
def user():
    return render_template('user.html', users = users)

if __name__ == '__main__':
    app.run(debug=True)

