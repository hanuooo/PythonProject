from random import randint
import random
# from random import shuffle
#
# randomNumber = [su for su in range(1,11)]
# random.shuffle(randomNumber)
# print(randomNumber)
#
# sample = randomNumber[0:3]
# print(sample)
# shuffle = random.sample[0:3]
# print(shuffle)
#
# def sampling():
#     random.shuffle(randomNumber)
#     sample = sorted(randomNumber[0:5])
#     print(sample)

mylist01 = list()
for idx in range(1, 6):
    mylist01.append(random.randint(1, 10))
print('방법 01 리스트의 append 사용하기 : %s' % mylist01)

mylist02 = [random.randint(1, 10) for idx in range(1, 6)]
print('방법 02 List Comprehension 사용하기 : %s' % mylist02)

somedata = [idx for idx in range(1, 11)]
result = random.sample(somedata, 3)
print('sample() 함수 사용하기 : %s' % result)

random.shuffle(somedata)
print('shuffle() 함수와 슬라이싱 : %s' % somedata[0:3])

# 랜덤 정수 생성 연습
# 1~100 사이 랜덤 정수를 10개 리스트에 저장한 뒤 출력해 보세요.
# 단, 동일한 숫자가 여러 번 나오면 안됩니다.
#

oneHundred = [su for su in range(1, 101)]
random.shuffle(oneHundred)
hundred = oneHundred[0:10]
print(hundred)

# 메뉴 랜덤 추천하기
# 다음 메뉴 중에서 오늘 점심 메뉴를 1개 추천하세요.
menu = ['김치찌개', '제육볶음', '돈까스', '파스타', '떡볶이', '초밥', '김밥']

# print(random.choice(menu))
print('오늘 점심 메뉴 \'%s\' ' % menu[random.randint(0, len(menu) - 1)])

# 순서 섞기(shuffle)
# 다음 학생들의 시험 발표 순서를 무작위로 정해 보세요.
students = ['민수', '지우', '하은', '준서', '다현', '서준', '유진']

random.shuffle(students)
print('발표 순서 : %s' % students[0:6])



# 무작위 표본 추출(sample)
# 다음 회사의 직원 목록에서 랜덤하게 4명만 뽑아 프로젝트 TF팀을 만들어 보세요.
member_su = 4
employee = ['홍길동','김철수','이영희','박민지','최현우','송다인','정윤호','백지현']

sampling = random.sample(employee, member_su)
print('프로젝트 TF팀 : %s ' % sampling)


# 아래 학생 리스트에서 무작위로 1명을 뽑아 오늘 발표 담당자로 선정하세요.
students = ['진우', '현아', '수민', '도윤', '예린', '현수', '수진']
random.shuffle(students)
print ('오늘 발표 담당자 : \'%s\'' % students[0])