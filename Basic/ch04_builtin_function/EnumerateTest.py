fruits = ['사과', '감', '오렌지', '한라봉', '바나나']
for (index, value) in enumerate(fruits, start=1):
    message = '%d 번째 품목은 \'%s\' 입니다.' % (index, value)
    print(message)
# end for
print('-'*30)
for item in enumerate(fruits, start=1):
    message = '%d 번째 품목은 \'%s\' 입니다.' % (item[0], item[1])
    print(message)
# end for
print('-'*30)

print('* 기호는 가변 매개 변수로 인식이 되며, 내부에서 tuple로 처리됩니다.')
for item in enumerate(fruits):
    # message = '{}번째 값 : {}'.format(item[0], item[1])
    message = '{}번째 값 : {}'.format(*item)
    print(message)
# end for
print('-'*30)

coffees = ['아메리카노', '카페라떼', '카푸치노']
price = [5000, 6000, 5500]

for (index ,value) in enumerate(coffees):
    message = '\'%s\' 의 단가는 %d원 입니다.' % (coffees[index], price[index])
    print(message)
# end for
print('-'*30)


