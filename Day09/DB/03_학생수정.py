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

try:
    with conn.cursor() as cursor:
        sql = " update 학생 "\
            + " SET std_id = %s "\
            + "     ,name = %s "\
            + "     ,tel = %s "\
            + "     ,upd_date = now() "\
            + " WHERE std_id = %s "
        result = cursor.execute(sql, (std_id, name, tel, std_id))
        print('{}행의 데이터 수정 완료'.format(result))
    
    # 변경사항 적용
    conn.commit()

except pymysql.MySQLError as e:
    print("데이터 등록 중 에러 발생 : ", e)
finally:
    conn.close()