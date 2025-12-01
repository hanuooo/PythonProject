# 초기 데이터
breads = {'바게트':100, '치아바타':200, '호밀빵':300, '베이글':400}

# '스콘'이 존재하지 않으면 150원으로 추가하세요.
# 치아바타 가격을 250원으로 수정하세요.
# 단가 300원짜리가 존재하는지 체크하고, 없으면 '브리오슈'를 300원으로 추가하세요.
# 리스트 반복문을 사용하여 다음 항목을 추가하세요
# newItems = ['통밀빵', '옥수수빵', '크랜베리빵']
# 다음 항목에 대하여 존재하면 출력, 그렇지 않으면 예외 처리를 수행해 주세요.
# targetList = ['옥수수빵', '단팥빵']
# get() 사용 기본값 : '프레첼'을 조회해 보되, 없는 경우 기본 값을 200으로 출력해 보세요.
# items()를 사용하여 전체 항목을 출력해 보세요.
# 조건에 따른 가격 조정 : '바게트', '치아바타'는 50원 인상, '스콘'은 50원 인하를 수행하세요.

targetItem = '스콘'
if targetItem not in breads:
    breads[targetItem] = 150
print(breads)

breads['치아바타'] = 250
print(breads)

price = 300
if price in breads.values():
    print("300원짜리 빵이 있습니다.")
else:
    print("300원짜리 빵이 없어서 추가합니다.")
    breads['브리오슈'] = 300
print(breads)


newItems = ['통밀빵', '옥수수빵', '크랜베리빵']
for idx in range(len(newItems)):
    breads[newItems[idx]] = (idx + 5) * 100

print(breads)

targetList = ['옥수수빵', '단팥빵']
for key in targetList:
    try:
        price = breads[key]
        print("품명 : %s, 가격 : %d" % (key, price))
    except KeyError:
        print("'%s' 키가 없어서 신규 추가합니다." % key)
        breads[key] = 350

print(breads)

targetItem = '프레첼'
price = breads.get(targetItem, 200)
print("품명 : %s, 가격 : %d" % (targetItem, price))


for (key, value) in breads.items():
    print("항목 %s의 가격은 %d원입니다." % (key, value))


for key in breads.keys():
    if key in ['바게트', '치아바타']:
        breads[key] += 50
    elif key == '스콘':
        breads[key] -= 30

# 조정 후 출력
for key, value in breads.items():
    print("품명 : %s, 가격 : %d" % (key, value))

# breads = {'바게트':100, '치아바타':200, '호밀빵':300, '베이글':400}
#
# findData = '스콘'
# boolean = findData in breads
# if boolean:
#     print('키\'%s\'(이)가 존재 합니다')
# else:
#     print('키\'%s\'(이)가 존재하지 않습니다')
#     breads[findData] = 150
# # end if
#
# print('키(key) 목록 : ', breads.keys())
# print('값(value) 목록 : ', breads.values())
#
# price = 300
# boolean = price in breads.values()
# if not boolean:
#     print('단가\'%d\'원 짜리가 존재하지 않습니다.' % price)
#     breads['브리오슈'] = 300
# else:
#     print('단가\'%d\'원 짜리가 존재합니다.'% price)
# # end if
#
# newItems = ['통밀빵', '옥수수빵', '크랜베리빵']
# for idx in range(len(newItems)):
#     breads[newItems[idx]] = (idx+7) * 100
# # end for
#
# targetList = ['옥수수빵', '단팥빵']
# for key in targetList:
#     try:
#         message = '품명 : %s, 가격 : %d ' % (key, breads[key])
#         print(message)
#
#     except KeyError:
#         print('%s 키가 존재하지않아서 신규추가합니다.' % key)
#         breads[key] = 500
#     # end try
#
#     print(type(breads))
#     print('요소 개수 : %d' % len(breads))
#     print(breads)
