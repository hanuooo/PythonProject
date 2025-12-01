coffees = dict() # {} 기호도 가능

coffees['에스프레소'] = 1000 # 신규 추가

coffees['에스프레소'] = 1500 # 이미 존재하면 덮어 쓰기
coffees['카페라떼'] = 2000
coffees['카푸치노'] = 3000
coffees['마키야또'] = 4000

findData = '카페라떼'
boolean = findData in coffees

if boolean:
    print('키 \'%s\'(이)가 존재합니다.' % findData)
else:
    print('키 \'%s\'(이)가 존재하지 않습니다.' % findData)
# end if

# not 키워드는 값을 부정할 때 사용합니다.
findData = '핫초코'
boolean = findData in coffees
if not boolean:
    print('키 \'%s\'(이)가 존재하지 않습니다.' % findData)
    coffees[findData] = 5000 # 존재하지않는 키,값 추가하는 방법
else:
    print('키 \'%s\'(이)가 존재합니다.' % findData)
# end if

print('키(key) 목록 : ', coffees.keys())
print('값(value) 목록 : ', coffees.values())

price = 6000
boolean = price in coffees.values()
if boolean:
    print('단가 \'%d\'짜리 품목이 존재합니다.' % price)
else:
    print('단가 \'%d\'짜리 품목이 않습니다.' % price)
    coffees['아이스커피'] = 6000
# end if

listCoffee = ['바닐라라떼', '라벤더', '딸기라떼', '콜드브루']
for idx in range(len(listCoffee)):
    coffees[listCoffee[idx]] = (idx+7) * 1000
# end for

findData = '핫초코'
print('%s의 가격은 %d입니다.' % (findData, coffees[findData])) # coffees[findData] 읽기작업 => [key]

targetList = ['라벤더','우유커피']
for key in targetList:
    try:
        message = '품명 : %s, 가격 : %d ' % (key, coffees[key])
        print(message)

    except KeyError:
        print('%s 키가 존재하지않아서 신규추가합니다.' % key)
        coffees[key] = 5000
# end try
# end for

findData = '둥굴레차'
price = coffees.get(findData, 3000) # 없으면 기본 값으로 대체
print('품명 : %s, 가격 : %d ' % (findData, price))

findData = '아이스커피'
popItem = coffees.pop(findData)
message = '삭제된 품목 %s의 이전 가격은 %d원이었습니다.'
print(message % (findData, popItem))

del coffees['에스프레소']

for (key, value) in coffees.items():
    message = '품목 %s의 단가는 %d원 입니다.' % (key, value)
    print(message)
# end for

# 전체 목록 출력
# 단, '카페라떼'와 '카푸치노'는 500원 인상
# '핫초코'는 500원 인하
print('전체 목록 출력')
for key in coffees.keys():
    if key == '카페라떼' or key == '카푸치노':
        coffees[key] += 500
    elif key == '핫초코':
        coffees[key] -= 500
    else:
        pass
    # end if

    message = '품명 : %s, 가격 : %d ' % (key, coffees[key])
    print(message)
# end for

coffees.clear()

if len(coffees) == 0:
    print('my dict is empty')
else:
    print('my dict is not empty')
# end if

print(type(coffees))
print('요소 개수 : %d' % len(coffees))
print(coffees)
