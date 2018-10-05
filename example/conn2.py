
import pymysql

"""

## 데이터베이스 생성 (create database)

conn = pymysql.connect(host='localhost', user='root', password='qwer1234!', charset='utf8mb4')

try:
    with conn.cursor() as cursor:
        sql = 'create database test1'
        cursor.execute(sql)
    conn.commit()
finally:
    conn.close()
"""

"""
## 테이블 생성 (create table)

conn = pymysql.connect(host='localhost', user='root', password='qwer1234!', db='test1', charset='utf8mb4')

try:
    with conn.cursor() as cursor:
        sql='''
         create table t_user (
            id INT UNSIGNED NOT NULL AUTO_INCREMENT,
            name VARCHAR(20) NOT NULL, 
            address VARCHAR(30) NOT NULL,
            phone INT(20) NOT NULL,
            PRIMARY KEY(id)
            );'''
        cursor.execute(sql)
    conn.commit()
finally:
    conn.close()
"""

"""
## 데이터 삽입 (insert)

conn = pymysql.connect(host='localhost', user='root', password='qwer1234!', db='test1', charset='utf8mb4')

try:
    with conn.cursor() as cursor:
        sql = "insert into t_user (id, name, address, phone) " \
              "values ('1','SINAE','서울시갈현동', '0101231234')"
        cursor.execute(sql)

    conn.commit()
    print(cursor.lastrowid)

finally:
    conn.close()
"""

"""
## 데이터 조회 (select)

conn = pymysql.connect(host='localhost', user='root', password='qwer1234!', db='test1', charset='utf8mb4')

try:
    with conn.cursor() as cursor:
        sql = 'select * from t_user where name=%s '
        cursor.execute(sql, ('SUJIN'))
        result = cursor.fetchone()
        print(result)

finally:
    conn.close()
"""

"""
## 데이터 수정(update)

conn = pymysql.connect(host='localhost', user='root', password='qwer1234!', db='test1', charset='utf8mb4')

try:
    with conn.cursor() as cursor:
        sql = 'update t_user set address= %s where id=1'
        cursor.execute(sql, '서울시강남구')
    conn.commit()
    print(cursor.rowcount)

finally:
    conn.close()
"""

## 데이터 삭제(delete)

conn = pymysql.connect(host='localhost', user='root', password='qwer1234!', db='test1', charset='utf8mb4')

try:
    with conn.cursor() as cursor:
        sql = 'delete from t_user where id=%s'
        cursor.execute(sql,1)
    conn.commit()
    print(cursor.rowcount)

finally:
    conn.close()



