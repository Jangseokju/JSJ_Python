import os
import pandas as pd

# 파일 경로 입력
program_path = os.path.abspath(__file__)
path = os.path.dirname(program_path)
input_file = path + '/input/' + input('입력 파일 : ')
output_file = path + '/output/' + input('출력 파일 : ')

# 엑셀 파일 입력
data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)

# index로 열 선택

# data_frame.iloc[ 행, 열 ]
data = data_frame.iloc[ : , [1, 3] ]

# 엑셀 파일 출력
writer = pd.ExcelWriter(output_file)
data.to_excel(writer, sheet_name='out_january_2013', index=False)
writer.close()
