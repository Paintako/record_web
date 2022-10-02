import sqlite3

db = sqlite3.connect('Test.db',check_same_thread=False)

cur = db.cursor()

'''
CREATE TABLE 資料表名稱 (
  欄位1 INT,
  欄位2 VARCHAR(50),
  欄位3 TEXT,
  ···
); //建立資料表 
'''
# 創建 MESSAGE 這個table
# cur.execute(''' CREATE TABLE IF NOT EXISTS "MESSAGE"(
#         "ID"              INTEGER   NOT NULL,
#         "CHECK"           TEXT   NOT NULL,
#         "MESSAGE"         TEXT   NOT NULL);''')

# print("table created")
# # 放資料進去db
# a=20
# b="123"

# message1 = "hgdflkjgsfd"
# message2 = "asfjdgfmghojpke;mf"

# cur.execute('''INSERT OR IGNORE INTO MESSAGE("ID","CHECK","MESSAGE") VALUES(?, ?, ?)''',(a,b,message1))
# cur.execute('''INSERT OR IGNORE INTO MESSAGE("ID","CHECK","MESSAGE") VALUES(?, ?, ?)''',(a,b,message2))

#cur.execute('''INSERT INTO MESSAGE("ID","CHECK","MESSAGE") VALUES(?, ?, ?)''',(a,b,c))
# 從DB中拿資料
result = cur.execute('''SELECT * FROM MESSAGE''')
for items in result:
    print(items)

db.commit()
db.close()