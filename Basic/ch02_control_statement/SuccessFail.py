middle = int(input('중간 고사 : '))
final = int(input('기말 고사 :'))
jumsu = middle * 0.4 + final * 0.6

if jumsu >= 70:
    success = 'pass'
else:
    success = 'fail'
# if end

print('중간 고사 점수 : {}'.format(middle))
print('기말 고사 점수 : {}'.format(final))
print('점수 : {}'.format(jumsu))
print('합격 여부 : {}'.format(success))
