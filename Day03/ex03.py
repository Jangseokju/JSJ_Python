# 자판기에 금액을 입력하고
# 커피의 잔 수에 따라서 남은 금액을 출력하세요.

# 한잔 : 300원
# 1400원
# 출력
# 커피 1잔, 1100원
# 커피 2잔, 800원
# 커피 3잔, 500원
# 커피 4잔, 200원

money=input('입력금액 : ')
money = int(money)

i=0

while money // 300 > 0:
    money = money-300
    i+=1
    print("커피 {}잔, {}원".format(i, money))
