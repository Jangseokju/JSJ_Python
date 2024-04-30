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
    # 커서 생성
    with conn.cursor() as cursor:
        # 데이터 등록 쿼리
        sql = " DELETE FROM 학생 "\
            + " WHERE std_id = %s "
        
        result = cursor.execute(sql, (std_id))
        print('{}행의 데이터 등록 완료'.format(result))
    
    # 변경사항 적용
    conn.commit()

except pymysql.MySQLError as e:
    print("데이터 등록 중 에러 발생 : ", e)
finally:
    conn.close()