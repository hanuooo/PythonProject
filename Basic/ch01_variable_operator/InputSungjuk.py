name = input('이름 입력 : ')
grade = int(input('학년 입력 : '))
ban = int(input('반 입력 : '))
kor = float(input('국어 입력 : '))
eng = float(input('영어 입력 : '))
math = float(input('수학 입력 : '))

total = (kor + eng + math)
average = total / 3.0

print('\n이름 :%s ' % (name))
print('{}학년 {}반'.format(grade, ban))
print('국어 :%6.2f' % (kor))
print('영어 :%6.2f' % (eng))
print('수학 :%6.2f' % (math))
print('총점 :%6.2f' % (total))
print('평균 :%6.2f' % (average))





# message ='이름 : {}\n국어 : {}\n 영어 : {}\n 수학 : {}\n 총점 : {}\n 평균 : {}'
# print(message.format(name,gook,eng,math,total,average))

