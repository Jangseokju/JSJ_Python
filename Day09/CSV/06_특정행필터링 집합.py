import csv
import sys

path ='C:/ALOHA/SEOKJU/GIT/JSJ_Python/Day09/CSV/'
input_file = path + '/input/' + input('입력 파일 : ')
output_file = path + '/output/' + input('출력 파일 : ')

important_dates = ['1/20/14', '1/30/14']

with open(input_file, 'r', newline='') as csv_in_file:
	with open(output_file, 'w', newline='') as csv_out_file:
		filereader = csv.reader(csv_in_file)
		filewriter = csv.writer(csv_out_file)
		header = next(filereader)
		filewriter.writerow(header)
		
		for row_list in filereader:
			a_date = row_list[4]
			if a_date in important_dates:
				filewriter.writerow(row_list)