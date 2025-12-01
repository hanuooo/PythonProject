name = '김철수'
fruit = '사과'
gaesu = 8
su01 = 4
su02 = 9
su03 = -5 # abs 함수 사용하여 절대값 변경
a = 2.0
b = 3.0
rate = 0.4567

message = '%s이(가) %s를 %d개 먹었습니다'
print(message % (name, fruit, gaesu))

message = '%d 곱하기 %d는 %d입니다.'
print(message % (su01, su02, (su01 * su02)))

message = '%f의 %f의 제곱은 %f 입니다'

print('%를 표현하려면 %%를 표시해야 합니다.')
print(message % (a, b,(pow(a ,b))))

print('비율 : %f%%' % (rate * 100))