coffee01 = ('아메리카노', '카페라떼')
coffee02 = ('콜드브루', '아이스커피')
# 소괄호 없이 콤마로 연결하면 무조건 tuple 입니다.
coffee03 = '카푸치노', '마키야또'

print('자료형 타입 : ', end='')
print(type(coffee01))

mylist = ['바닐라라떼', '플랫화이트']
coffee04 = tuple(mylist)

# + 기호를 사용하여 기존요소에 새로운 요소를 추가합니다.
coffees = coffee01 + coffee02 + coffee03 + coffee04 + ('에스프레소',)  # 문자열로 구성된 tuple 콤마필수

length = len(coffees)
print('요소 개수 : % d' % length)

# 1번째 요소를 '고구마라떼'로 변환해보세요
# coffees[1] = '고구마라떼' # tuple은 쓰기 작업 불가능.

# 인덱싱
print('앞에서 2번째 요소 : %s' % coffees[2])
print('뒤에서 1번째 요소 : %s' % coffees[-1])

# 슬라이싱
# coffees[start:end:step] : start부터 시작하여 end 직전까지 step 단계씩 슬라이싱하세요.
print('1번째~3번째까지의 요소 :', end='')
print(coffees[1:4])
print('3번째 이후의 요소 :', end='')
print(coffees[3:])
print('0번째~3번째 이전까지의 요소 :', end='')
print(coffees[:3])

print('짝수 요소 :', end='')
print(coffees[0::2])
print('홀수 요소 :', end='')
print(coffees[1::2])
print('전부 출력 :', end='')
print(coffees[::])

mycount = coffees.count('아메리카노')
print('아메리카노의 개수 : %d ' % mycount)

myindex = coffees.index('콜드브루')
print('콜드브루의 인덱스 번호 : %d ' % myindex)

