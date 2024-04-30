
import pandas as pd 

import tkinter as tk
from tkinter import filedialog

# 입력 파일 선택 버튼 클릭 시,
def open_input_file():
    print('입력 파일 선택...')
    # 파일 선택 상자에서 파일이름 가져오기
    filename = filedialog.askopenfilename()
    if filename:
        # 파일명 지정
        input_file.set(filename)


# 출력 파일 선택 버튼 클릭 시,
def open_output_file():
    print('출력 파일 선택...')
    # 파일 선택 상자에서 파일이름 가져오기
    filename = filedialog.asksaveasfilename()
    if filename:
        # 파일명 지정
        output_file.set(filename)

# 실행 버튼
def run():
    print('입력 파일 경로 : ' + input_file.get())
    print('출력 파일 경로 : ' + output_file.get())
    print('데이터 분석을 시작합니다...')
    work()

# 화폐 형식 기호
def format_th(x):
    return '${:,.2f}'.format(x)
    # : 시작기호
    # , 천단위 구분기호
    # .n : 소수점 아래 개수
    # f 는 float (실수)
# 데이터 분석
def work():
    # 엑셀 통합 문서의 모든 시트를 데이트프레임으로 반환
    data_frame = pd.read_excel(input_file.get(), sheet_name=None, index_col=None)

    # ✅ TODO :분석
    data = []
    for worksheet_name, sheet in data_frame.items():
        # 필터링 조건 : Sale Amount > 2000.0
        condition = sheet['Sale Amount'].replace('$','').replace(',','') \
                    .astype(float) > 2000.0
        result_sheet = sheet[condition]
        result_sheet['Sale Amount'] = result_sheet['Sale Amount'].map( format_th )
        data.append( result_sheet )
    filter_data = pd.concat(data, axis=0, ignore_index=True)
    # pd.concat( 결합할 데이터, axis=결합방향(0:수직,1:수평), ignore_index=인덱스무시여부)

    # 엑셀 출력 객체
    writer = pd.ExcelWriter(output_file.get())
    # 데이터프레임을 엑셀 파일로 저장 *index는 미사용
    filter_data.to_excel(writer, sheet_name='total_worksheets', index=False)
    # 출력 객체 해제
    writer.close()



# 윈도우 화면 생성
window = tk.Tk()
window.title('GUI 프로그램')

# 창 크기 지정
window.geometry('600x300')

# 라벨 생성
label = tk.Label(window, text="GUI 프로그램 라벨", padx=20, pady=10)
label.pack()

# 입력 상자 생성 - 입력 파일 경로
input_file = tk.StringVar()         # 문자열 변수 
input_entry = tk.Entry(window, textvariable=input_file, width=100)
input_entry.pack()

# 버튼 - 입력 파일 선택 버튼
input_button = tk.Button(window, text="입력 파일 선택", command=open_input_file)
input_button.pack()


# 입력 상자 생성 - 출력 파일 경로
output_file = tk.StringVar()         # 문자열 변수 
output_entry = tk.Entry(window, textvariable=output_file, width=100)
output_entry.pack()

# 버튼 - 입력 파일 선택 버튼
output_button = tk.Button(window, text="출력 파일 선택", command=open_output_file)
output_button.pack()

# 실행 버튼
run_button = tk.Button(window, text="실행", padx=10, pady=10, command=run)
run_button.pack()

window.mainloop()