# 중첩 반복문
# : 반복문 안에 또 하나의 반복문을 작성

# 구구단 전체 출력
# 2~9 : i
# 1~9 : j
for i in range(2,10):
    for j in range(1,10):
        print('{} x {} = {}'.format(i,j,i*j))
    print()