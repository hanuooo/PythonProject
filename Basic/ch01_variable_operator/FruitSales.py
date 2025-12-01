applePrice = 1000
appleQty = 3
gamPrice = 500
gamQty = 10
money = 10000
change = money - (applePrice * appleQty + gamPrice * gamQty)

print('구매 정보')
print('사과 {}개 구매, 가격:{}'.format(appleQty, applePrice*appleQty))
print('감 {}개 구매, 가격:{}'.format(gamQty, gamPrice*gamQty))

print('\n결재 정보')
print('내신 금액 : %d' % money)
print('잔돈 : %d' % change)