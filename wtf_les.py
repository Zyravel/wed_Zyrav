from flask import Flask, request, render_template
import sqlite3
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired


class MyForm(FlaskForm):
    id = IntegerField('id', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    bill = IntegerField('bill', validators=[DataRequired()])
con = sqlite3.connect('web_base.db', check_same_thread=False)
cur = con.cursor()
# res = cur.execute(f'select * from meat')
# result = res.fetchall()
# con.commit
app = Flask(__name__)

# @app.route('/add_u')
# def add_u():
#     id = request.args.get('id')
#     name = request.args.get('name')
#     bill = request.args.get('bill')
#     new_text = (id, name, bill)

#     cur.execute(f'INSERT INTO meat(id,name,bill) VALUES (?, ?, ?)', new_text)
#     con.commit()
#     res = curs.execute(f'SELECT * FROM meat')
#     return res.fetchall()


# @app.route("/")
# def hello():
#     return render_template('main.html')

# @app.route('/x')
# def re():

#     return render_template('test.html', t = result)

@app.route("/wt", methods = ['GET', 'POST'])
def wt():
    form = MyForm()
    if form.validate_on_submit():
        res_id = form.data['id']
        res_name = form.data['name']
        res_bill = form.data['bill']
        new_text = (res_id, res_name, res_bill)

        cur.execute(f'INSERT INTO meat(id, name, bill) VALUES (?, ?, ?)', new_text)
        con.commit()
        return "ok"
    return render_template('wtftest.html', form = form)


if __name__ == '__main__':
    app.config['WTF_CSRF_ENABLED'] = False
    app.run()
