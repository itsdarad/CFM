from flask import Flask
from flask import request
import sqlite3

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! My name is Josh and I have the team that is going to win this years CodeLinc!!!!!</p>"

@app.route("/user", methods=['GET', 'POST'])
def first():
    if request.method == 'POST':
        u_name = request.form['u_name']
        # body = request.get_json()
        # name = body['name']
        # id = body['id']
        # print(name)
        con = sqlite3.connect("CFMDB.db")
        cur = con.cursor()
        res = cur.execute('SELECT lastname FROM CFMdata WHERE firstname = "{}"'.format(u_name))
        stuff = res.fetchone()


        
        return 'Hi, your last name is: ' + stuff[0          ]
    else:
        return 'this was not a POST'

@app.route("/user/<username>")
def show_user(username):
    return "Hi " + username + ", I hope you are having a good night"
