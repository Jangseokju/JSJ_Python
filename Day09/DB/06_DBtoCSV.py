# pip install pymysql
import pymysql
import csv
import os

program_path = os.path.abspath(__file__)
# 디렉터리 경로 - 이 안의 input, output 폴더에서 입출력한다.
path = os.path.dirname(program_path)

# 입력 : csv
output_file = path + '/output/' + input('입력 파일 : ')
# 출력 : DB

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
        sql = "SELECT * FROM sample"
        cursor.execute(sql)        

        samplelist = cursor.fetchall()

        with open(output_file, 'w', newline='', encoding='UTF-8') as csv_out_file:
            # csv_out_file 파일을 ',' 구분자 쓰기모드로 CSV 파일 객체 생성
            filewriter = csv.writer(csv_out_file, delimiter=',')

            header = ('학번', '이름', '주소', '전화번호')
            filewriter.writerow(header)

            for sample in samplelist:
                std_id = sample.get('학번')
                name = sample.get('이름')
                address = sample.get('주소')
                tel = sample.get('전화번호')

                row = ( std_id, name, address, tel)

                filewriter.writerow(row)

except pymysql.MySQLError as e:
    print('MySQL 에러 :', e)
finally:
    conn.close()