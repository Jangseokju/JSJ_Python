s = "안녕하세요"

# 문자열 선택 연산자    : [index]
# 인덱싱
# index 는 0부터 시작하는 순서번호
# 한 줄 복사 alt + shift + 아래 방향키
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])

# 슬라이싱
# [시작index : 끝index+1]
print(s[0:2])   # 안녕
print(s[2:])    # 하세요
print(s[:2])    # 안녕

# 안녕하세요    : index(0~4)
# 주석 : ctrl + /
# print(s[100])   # 인덱스 범위 바깥의 번호를 입력한 에러

# 문자열의 길이 - len
print("문자열의 길이 :" + str( len(s)) )