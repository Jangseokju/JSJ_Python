import csv
import sys

path ='C:/ALOHA/SEOKJU/GIT/JSJ_Python/Day09/CSV/'
input_file = path + '/input/' + input('입력 파일 : ')
output_file = path + '/output/' + input('출력 파일 : ')

my_columns = [0, 3]

with open(input_file, 'r', newline='') as csv_in_file:
	with open(output_file, 'w', newline='') as csv_out_file:
		filereader = csv.reader(csv_in_file)
		filewriter = csv.writer(csv_out_file)
		for row_list in filereader:
			row_list_output = [ ]
			# my_columns 리스트 반복 - index_value : 0, 3
			for index_value in my_columns:
				# row_list[0] : 공급자명(supplier name)
				# row_list[3] : 가격(cost)
				row_list_output.append(row_list[index_value])
			filewriter.writerow(row_list_output)