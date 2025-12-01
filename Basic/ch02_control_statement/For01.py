total = 0
for i in range(1, 11):
    total += i
# end for
print('총합01 : %d' % total)

total = 0
for i in range(1, 101, 3):
    total += i
print('총합02 : %d' % total)

total = 0
for i in range(97, 1, -5):
    total += i
print('총합 03 : %d' % total)

total = 0
for i in range(1, 97, 5):
    total += i**2 # m**n = m의 n제곱 = m*m 과 동일
print('총합 04 : %d' % total)

total = 0
for i in range(1, 6):
    total += i*(i+1)
print('총합05 : %d' % total)