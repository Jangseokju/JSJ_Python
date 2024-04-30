# pip install pymysql
import pymysql

# mysql 서버에 접속
conn = pymysql.connect(
    host='127.0.0.1',
    user='SEOKJU_PYTHON',
    password='s162596j!!',
    database='joeun',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

# try:
    # if conn.ping(reconnect=)

try:
    with conn.cursor() as cursor:
        sql = "SELECT * FROM 학생"
        cursor.execute(sql)        

        students = cursor.fetchall()

        for student in students
        print(student)
except pymysql.MySQLError as e:
    print('MySQL 에러 :', e)
finally:
    conn.close()