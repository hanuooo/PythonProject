mylist01 = [idx for idx in range(1, 5)]
print(mylist01)

mylist02 = [idx for idx in range(1, 6)]
print(mylist02)

# 1, 4, 7, ..., 100
mylist03 = [idx for idx in range(1, 101, 3)]
print(mylist03)

mylist04 = [idx for idx in range(1, 101, 3) if idx%10 == 0]
print(mylist04)

exam_jumsu = [75, 30, 85, 50] # 합격 기준은 60점 이상
mylist05 = [jumsu for jumsu in exam_jumsu if jumsu >= 60]
print(mylist05)
print(f'총{len(mylist05)}명 합격')

# 다음 항목들을 이용하여 사전으로 만들어 보세요.
# 다음 과일은 튜플(Tuple) 요소 3개를 담고 있는 리스트입니다.
fruits = [('바나나', 10), ('사과', 20),('오렌지', 30)]

# dict(사전) comperhension
mydict01 = {item[0]:item[1] for item in fruits} # 인덱싱
print(mydict01)

# 학생들의 시험 점수를 사전으로 만들어 보세요.
# {'이문식': (80, 90, 50), '강수현':  (50, 60, 80), '윤정혁': (70, 40, 60)}
students = [
    ('이문식', 80, 90, 50),
    ('강수현', 50, 60, 80),
    ('윤정혁', 70, 40, 60)
    ]

mydict02 = {one[0]:one[1:] for one in students} # 슬라이싱
print(mydict02)

# 점수들의 총합을 사전의 value로 만들어 보세요.
# sum 함수는 파이썬 내장 함수 중의 하나
# {'이문식': 220, '강수현': 190, '윤정혁': 170}
mydict03 = {one[0]:sum(one[1:]) for one in students} # sum 총합 후 결과반환
print(mydict03)