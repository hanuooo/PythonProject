name = input('이름 입력 : ')
kor = int(input('국어 점수 입력 : '))
eng = int(input('영어 점수 입력 : '))
math = int(input('수학 점수 입력 : '))

total = kor + eng + math
average = total / 3.0

# 학점은 다중 택일 if
if average >= 90 :
    hakjum = 'A'
    comment = '참 잘 하셨습니다.'
elif average >= 80 :
    hakjum = 'B'
    comment = '참 잘 하셨습니다.'
elif average >= 70 :
    hakjum = 'C'
    comment = '조금만 더 노력하세요.'
elif average >= 60 :
    hakjum = 'D'
    comment = '조금만 더 노력하세요'
else:
    hakjum = 'F'
    comment = '다음 학기에 재수강하세요.'
# end if

print('%s님의 정보' % name)
print('국어 : %d, 영어 : %d, 수학 : %d' % (kor, eng, math))
print('총점 : %d ' % total)
print('평균 : %.2f ' % average)
print('학점 : %c ' % hakjum) # ! %s
print('코멘트 : %s ' % comment)