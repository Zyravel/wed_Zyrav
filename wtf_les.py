from flask import Flask, render_template
import sqlite3

con = sqlite3.connect('web_base.db')
cur = con.cursor()
res = cur.execute(f'select * from meat')
result = res.fetchall()
con.commit
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('main.html')

@app.route('/x')
def re():

    return render_template('test.html', t = result)


if __name__ == '__main__':
    app.run()