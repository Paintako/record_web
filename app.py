from email import message
from flask import Flask
from flask import render_template
from flask import request
import sqlite3
app = Flask(__name__) # 創建一個Flask的 instance

db = sqlite3.connect('Test.db',check_same_thread=False)
cur = db.cursor()
cur.execute(''' CREATE TABLE IF NOT EXISTS "MESSAGE"(
        "ID"              INTEGER   NOT NULL,
        "CHECK"           TEXT   NOT NULL,
        "MESSAGE"         TEXT   NOT NULL);''')

@app.route('/')
def index():
	result = cur.execute('''SELECT * FROM MESSAGE''')
	for items in result:
		print(items)
	return render_template('record.html')


@app.route('/',methods=['POST','GET']) # 這一行是告訴 ‘/’允許的method有什麼，GET不能拿掉，因為GET預設拿來訪問網頁的
def submit():
	if request.method =='POST':
		rst = dict(request.values)
		msg = rst['message']
		id = rst['message_id']
		print(id)
		if 'ch' in rst:
			check_var = 1
		else:
			check_var = 0
		cur.execute('''INSERT OR IGNORE INTO MESSAGE("ID","CHECK","MESSAGE") VALUES(?, ?, ?)''',(id,check_var,msg))
		db.commit()



	return render_template('record.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0',port='5000',debug=True)