"""
    문제02.csv 파일을 입력받아
    전화번호 컬럼의 데이터에 대하여
    전화번호 형식의 정규표현식으로 매칭되는
    데이터만 추출하시오.
"""

import pandas as pd
import sys

path ='C:/ALOHA/SEOKJU/GIT/JSJ_Python/Day09/CSV/'
input_file = path + '/input/' + input('입력 파일 : ')
output_file = path + '/output/' + input('출력 파일 : ')

data_frame = pd.read_csv(input_file)
pattern = re.compile(r'(?P<my_pattern_group>)^\d{2,3}-\d{3,4}-\d{4}$', re.I)
condition = data_frame['전화번호'].str.match(pattern)

data_frame_value_matches_pattern = data_frame.loc[condition, :]

data_frame_value_matches_pattern.to_csv(output_file, index=False)