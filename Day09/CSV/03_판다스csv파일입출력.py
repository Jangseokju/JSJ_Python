import sys
import pandas as pd

path ='C:/ALOHA/SEOKJU/GIT/JSJ_Python/Day09/CSV/'
input_file = path + '/input/' + input('입력 파일 : ')
output_file = path + '/output/' + input('출력 파일 : ')

data_frame = pd.read_csv(input_file)
print(data_frame)
# data_frame.to_csv(output_file, index=False)
data_frame.to_csv(ouput_file)