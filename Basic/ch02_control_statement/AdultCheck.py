name = input('이름 입력 : ')
age = int(input('나이 입력 : '))

# 변수 앞에 _를 붙여서 내부족으로 사용하는 보조 변수로 사용합니다.
_gender = int(input('성별 입력(숫자 1, 2, 3, 4 중 택일 : '))

if age > 19:
    adult = '성인'
else:
    adult = '미성년자'
# end if ( if문 끝 단락 구분 팁)

# 최종적으로 의미를 가지는 변수입니다.
if _gender == 1 or _gender ==3:
    gender = '남자'
else:
    gender = '여자'

print('이름 : %s' % name)
print('나이 : %d' % age)
print('성인 여부 : %s' % adult)
print('성별 : %s' % gender)
