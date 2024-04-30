"""
    supplier_data.csv 파일을 입력하여,
    Supplier Y 공급업체 또는 Supplier Z 공급업체라면 가격이 650 초과인
    Data를 문제01.csv 파일로 출력하시오.

"""

import pandas as pd
import sys

path ='C:/ALOHA/SEOKJU/GIT/JSJ_Python/Day09/CSV/'
input_file = path + '/input/' + input('입력 파일 : ')
output_file = path + '/output/' + input('출력 파일 : ')

data_frame = pd.read_csv(input_file)

data_frame['Cost'] = data_frame['Cost'].str.strip('$').astype(float)

공급업체 = data_frame['Supplier Name'].str
가격 = data_frame['Cost']

condition = 공급업체.contains('Y') | (공급업체.contains('Z') & (가격 > 650.0))

data_frame_value_meets_condition = data_frame.loc[condition, :]
data_frame_value_meets_condition.to_csv(output_file, index=False)