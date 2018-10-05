
## mysql database에 있는 테이블 불러오기 (select)


import pymysql

##example 01

#mysql Connection 연결
conn = pymysql.connect(host='localhost', user='root', password='qwer1234!', db='sakila', charset='utf8')

# Connection으로부터 Dictionary cursor 생성
curs = conn.cursor(pymysql.cursors.DictCursor)

#SQL문 실행
sql = "select * from actor where first_name = 'CUBA'"
curs.execute(sql)

#데이터 Fetch
rows = curs.fetchall()
for row in rows:
    print(row)
    print(row['first_name'], row['last_name'], row['last_update'])


conn.close()




##example 02

"""
#mysql Connection 연결
conn = pymysql.connect(host='localhost', user='root', password='qwer1234!', db='sakila', charset='utf8')

# Connection으로부터 Cursor 생성
curs = conn.cursor()

#SQL문 실행
sql = "select * from actor"
curs.execute(sql)

#데이터 Fetch
rows = curs.fetchall()
print(rows) #전체 rows

# connection 닫기
conn.close()
"""


