import sys
from xlrd import open_workbook

path = 'C:/ALOHA/SEOKJU/GIT/JSJ_Python/Day09/Excel/'
input_file = path + '/input/' + input('입력 파일 : ')
# input_file = sys.argv[1]

# open_workbook(파일 경로) : 지정한 엑셀 파일을 열어서 WorkBook 객체로 가져온다.
workbook = open_workbook(input_file)

# workbook.nsheets : 엑셀 파일내의 시트 개수
print('시트 개수 : ', workbook.nsheets)

# sheets()  : 모든 시트를 리스트로 반환
# - name    : 시트 이름
# - nrows   : 행 수
# - ncols   : 열 수
for worksheet in workbook.sheets():
	print("Worksheet name:", worksheet.name, "\t행 수:", \
			worksheet.nrows, "\t열 수:", worksheet.ncols)
