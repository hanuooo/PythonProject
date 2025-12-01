# RE !

# list comprehension을 활용한 문제
# 평균 이상 점수를 받은 학생 수 출력하기
scores = [55, 80, 92, 45, 68, 88]  # 평균 이상이면 '우수'

avg = sum(scores) / len(scores)
excellent = [jumsu for jumsu in scores if jumsu >= avg]

print(f'원본 데이터 : {scores}')
print(f'평균 : {avg}')
print(f'결과 데이터 : {excellent}')
print(f'평균 이상 학생 수: {len(excellent)}명')

# 나이가 18세 이상인 사람만 추출하여 몇 명인지 출력
ages = [12, 17, 18, 20, 35, 15]

adults = [age for age in ages if age >= 18]

print(f'\n원본 데이터 : {ages}')
print(f'결과 데이터 : {adults}')
print(f'성인 인원: {len(adults)}명')

# 양수만 골라서 개수 출력하기
numbers = [-5, 3, 0, 7, -2, 10, -8]

positive = [num for num in numbers if num > 0]

print(f'\n원본 데이터 : {numbers}')
print(f'결과 데이터 : {positive}')
print(f'양수 개수: {len(positive)}개')

# 짝수만 골라서 출력 및 개수 표시
data = [1, 4, 7, 10, 13, 16]

evens = [x for x in data if x % 2 == 0]

print(f'\n원본 데이터 : {data}')
print(f'결과 데이터 : {evens}')
print(f'짝수 개수: {len(evens)}개')

# 이름 리스트에서 3글자 이상인 이름만 추출
names = ["유나", "철수", "민지", "Tom", "Ann", "Jennifer"]

long_names = [person for person in names if len(person) >= 3]

print(f'\n원본 데이터 : {names}')
print(f'결과 데이터 : {long_names}')
print(f'3글자 이상 이름 수: {len(long_names)}개')
