import sqlite3

con = sqlite3.connect('web_base.db')
cur = con.cursor()
res = cur.execute(f'select * from meat')
result = res.fetchone()
print(result)