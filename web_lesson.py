from flask import Flask, request
import sqlite3
import json

con = sqlite3.connect("web_base.db",check_same_thread=False)
curs = con.cursor()
# res = curs.execute(f'SELECT * FROM meat')
# print(res.fetchall())


app = Flask(__name__)

@app.route("/")
def hi():
    return "WTF!"



@app.route("/user/<n>")
def hx(n):
    res = curs.execute(f'SELECT * FROM meat WHERE id = {n}')
    r = res.fetchone()

    return f'{r[1]}'


@app.route('/add_u')
def add_u():
    id = request.args.get('id')
    name = request.args.get('name')
    bill = request.args.get('bill')
    new_text = (id, name, bill)
    # res = curs.execute(f'SELECT * FROM meat')
    # return res.fetchall()
    curs.execute(f'INSERT INTO meat(id,name,bill) VALUES (?, ?, ?)', new_text)
    con.commit()
    res = curs.execute(f'SELECT * FROM meat')
    return res.fetchall()
    # return "id = {};name = {}; bill = {}".format(id, name, bill) 


app.run()