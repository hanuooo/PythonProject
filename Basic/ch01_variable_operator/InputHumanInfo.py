print('이름 입력 :', end = '')
name=input()

# 주의 사항 : input() 함수는 무조건 문자열로 취급합니다.
age=int(input('나이 입력 :')) # int : 정수형으로 형변환 필요

height=float(input('키 입력 : '))

print('\n% 포맷 코드 형식으로 출력')
print('이름 : %s' % name)
print('나이 : %d' % age)
print('키 : %.2f' % height)

print('\nfomat() 함수를 사용한 출력')
message = '제 이름은 {}이고, 나이는 {}세입니다.\n제 키는 {}cm입니다.'
print(message.format(name, age, height))