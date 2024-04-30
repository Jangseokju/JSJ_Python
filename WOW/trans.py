# 번역
# : googletrans 모듈을 사용하여 번역하는 프로그램
from googletrans import Translator
import os
# pip install googletrans==4.0.0-rc1


# 실행 프로그램의 경로
program_path = os.path.abspath(__file__)
# 디렉터리 경로 - 이 안의 input, output 폴더에서 입출력한다.
path = os.path.dirname(program_path)

# 텍스트 번역 함수
def translate_text(input_file, output_file, source_lang='en', target_lang='ko'):
    # 구글 번역 객체 생성
    translator = translator()

    # 파일 입력
    with open(input_file, 'r', encoding='utf-8') as file:
        input_text = file.read()
    # 번역
    translate_text = translator.translate(input_text, \
                                          src=source_lang, dest=target_lang)
    # 번역 결과 출력
    with open (output_file, 'w', encoding='utf-8') as file:
        file.write(translate_text.text)

input_file = path + '/' + input('입력 파일 : ')
output_file = path + '/' + input('출력 파일 : ')

translate_text(input_file, output_file)
print('번역 완료!')