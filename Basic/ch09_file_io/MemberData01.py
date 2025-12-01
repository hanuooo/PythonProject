print('파일을 읽기 모드로 오픈한다.')
# 읽을 파일
source = open('memdata01.csv', 'rt', encoding='utf-8')

# {부서이름:인원수}를 저장할 사전 객체
positionDict = dict()

print('\nreadlines() 함수는 모든 라인을 읽어서 리스트로 만들어 준다.')
linelists = source.readlines()
source.close()

totallist = []
for oneitem in linelists:
    mylist = oneitem.split(',')
    name = mylist[0]
    buseo = mylist[1]
    position = mylist[2]
    jumsu1 = float(mylist[3]) * 80 / 1000
    jumsu2 = float(mylist[4]) * 10 / 100
    jumsu3 = float(mylist[5]) * 10 / 100

    if buseo in positionDict:
        positionDict[buseo] += 1
    else:
        positionDict[buseo] = 1
    # end if
    total = jumsu1 + jumsu2 + jumsu3
    average = total / 3.0

    # %10.2f : 10은 넉넉한 임의의 숫자, .2은 소수점 2자리 까지 표시하려고...
    avg = float('%10.2f' % (average))

    sublist = (name, total, avg)
    totallist.append(sublist)
# end for

print('\n리스트 정보')
print(totallist)

print('\n사전 정보')
print(positionDict)

print('작업 종료')

# import csv
#
# # CSV 읽기
# data = []
# with open('memdata01.csv', mode='rt', encoding='utf-8') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         data.append(row)
#
# # -----------------------------------------
# # 1) 부서별 인원 수 출력
# # -----------------------------------------
# dept_count = {}
#
# for row in data:
#     dept = row[1]
#     dept_count[dept] = dept_count.get(dept, 0) + 1
#
# print("### 부서별 인원 수 ###")
# print(dept_count)
# print()
#
# # -----------------------------------------
# # 2) 직원 성적 계산
# # -----------------------------------------
# # 과목별 만점/가중치
# # 입사시험 1000점 → 80%
# # 외국어 100점 → 20%
# # 승진시험 100점 → 20%
#
# def calc_score(job, foreign, promo):
#     job = float(job)
#     foreign = float(foreign)
#     promo = float(promo)
#     return job * 0.08 + foreign * 0.20 + promo * 0.20
#
#
# print("### 직원별 종합 성적 ###")
# for row in data:
#     name = row[0]
#     score = calc_score(row[3], row[4], row[5])
#     print(f"{name}의 종합점수 : {score:.2f}")
# print()
#
# # -----------------------------------------
# # 3) 리스트 자료 생성 (예: [('강감찬', 77.2), ('김유신', 88), ...])
# # -----------------------------------------
# result_list = []
#
# for row in data:
#     name = row[0]
#     score = calc_score(row[3], row[4], row[5])
#     result_list.append((name, round(score, 1)))
#
# print("### 결과 리스트 ###")
# print(result_list)