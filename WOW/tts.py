# 텍스트를 음성으로 변환하는 라이브러리
# gtts
# TTS : Text To Speech
# STT : Speech To Text

from gtts import gTTS
import os

text = "집에 갈 시간입니다. 파이썬 엑셀 데이터 분석 시간입니다."
tts = gTTS(text=text, lang='ko')

tts.save('test.mp3')

os.system("test.mp3")