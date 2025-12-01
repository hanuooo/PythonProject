# coffees = [] # empty list
coffees = list() # 함수를 이용한 빈 리스트 생성

coffees.append('아메리카노')
coffees.append('콜드브루')
coffees.append('카푸치노')
coffees.append('바닐라라떼')
coffees.append('디카페인커피')
coffees.append('카페라떼')

count = len(coffees) # length
print('요소 개수 : %d' % count)

# 인덱싱
print('앞에서 2번째 요소 : %s' % coffees[2])
print('뒤에서 1번째 요소 : %s' % coffees[-1])

# 슬라이싱
# coffees[start:end:step] : start부터 시작하여 end직전까지 step 단계씩 슬라이싱하세요.
# start 안적으면 0 , step 안적으면 1 , end 안적으면 끝까지
print('1번째~3번째까지의 요소 : %s' % coffees[1:4])
print('3번째이후의 모든 요소 : %s' % coffees[3:])
print('0번째~3번째 이전까지의 요소 : %s' % coffees[:3])

coffees[1] = '고구마라떼' # 리스트는 쓰기 가능함

print('짝수 요소 : %s' % coffees[0::2]) # 0부터 2칸씩 = 짝수
print('홀수 요소 : %s' % coffees[1::2]) # 1부터 2칸씩 = 홀수
print('모든 요소 : %s' % coffees[::])

print('오름차순 정렬')
coffees.sort()
print(coffees)

print('내림차순 정렬')
coffees.sort(reverse=True)
print(coffees)