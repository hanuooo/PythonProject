name = '김철수'
age = 30
height = 175.3456789
adress = '마포'

print('이름 : %s' % (name))
print('나이 : %d' % (age))
print('키01 : %f' % (height)) # 실수의 기본 값은 소수점 6자리까지 표현
print('키02 : %.3f' % (height)) # 소수점 3자리까지
print('키03 : [%10.4f]' % (height)) # %m.nf : 전체 m자리, 소수점 n자리까지 출력
print('주소 : %s' % (adress))

message = '이름은 %s이고, 나이는 %d살입니다.'
print(message % (name, age))

su01 = 3
su02 = 5

message = '%d 더하기 %d는 %d입니다.'
print(message % (su01, su02,(su01 + su02)))

a = 2
b = 10
# pow(a, b)는 a의 b제곱을 해주는 내장 함수입니다.
print(pow(a, b))
message = '%d의 %d승은 %d입니다.'
print(message % (a, b, pow(a, b)))

hello = '안녕'
message = '[%10s]' % hello
print(message)

message = '[%-10s]' % hello
print(message)