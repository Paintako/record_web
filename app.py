from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__) # 創建一個Flask的 instance

message_list = list()

@app.route('/',methods=['POST','GET']) # 這一行是告訴 ‘/’允許的method有什麼，GET不能拿掉，因為GET預設拿來訪問網頁的
def submit():
	if request.method =='POST':
		print(request.values)
		message_list.append(request.values['message'])
		print(message_list)

	
	return render_template('record.html')



if __name__ == '__main__':
	app.run(host='0.0.0.0',port='5000',debug=True)