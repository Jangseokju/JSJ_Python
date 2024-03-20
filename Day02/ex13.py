# 조건 연산자
# x if 조건식 else y
# - 조건식의 결과가 참이면, x
#   거짓이면 y를 반환하는 함수

x=100
y=200

result = x if(x-y)>0 else y
print('result : {}'.format(result))