#!/usr/bin/env python3
import pandas as pd
import sys

path = 'C:/ALOHA/SEOKJU/GIT/JSJ_Python/Day09/Excel/'
input_file = path + '/input/' + input('입력 파일 : ')
output_file = path + '/output/' + input('출력 파일 : ')

# read_excel() : 엑셀 파일 읽어드려서, 데이터프레임으로 반환
data_frame = pd.read_excel(input_file, sheet_name='january_2013')

# ExcelWriter() : 쓰기 모드로 엑셀 파일 출력 객체 생성
writer = pd.ExcelWriter(output_file)

# to_excel(출력객체, sheet_name=시트이름, index=여부)
# : 데이터프레임을 엑셀 파일로 변환하여 저장하는 함수
data_frame.to_excel(writer, sheet_name='jan_13_output', index=False)

# save() : 엑셀 출력 객체로 파일 생성 및 저장
writer.close()