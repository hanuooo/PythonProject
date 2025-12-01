# mode는 읽기(read)/덮어 쓰기(write)/추가(append) 모드
print('파일에 커피 메뉴 기록합니다.')
filename = 'coffees_menu.txt'
coffee_file = open(file = filename, mode = 'wt', encoding = 'utf-8')
print(type(coffee_file))

coffees = ['아메리카노', '카페라떼', '카푸치노', '바닐라라떼', '모카']

for coffee in coffees:
    message = f'오늘 추천 커피는 {coffee} 입니다.'
    coffee_file.write(message)

coffee_file.close()
# end for '오늘 추천 커피는 XXX 입니다.

coffee_file02 = open(file = filename, mode = 'at', encoding = 'utf-8')

for idx in range(len(coffees)):
    if idx % 2 == 0:
        message = f'{idx} 번째 커피 {coffees[idx]} 풍미가 깊어요.'
    else:
        message = f'{idx} 번째 커피 {coffees[idx]} 부드럽게 즐기세요.'
    # end if

    coffee_file02.write(message)
# end for
coffee_file02.close()

print('반복문을 사용하여 커피 관련 파일 여러개 만들어 봅니다.')
print('파일 이름 : coffee01.txt ~ coffee05.txt')
for idx in range(1, 6):
    filename = 'coffee' + str(idx).zfill(2) + '.txt'
    with open(file=filename, mode='wt', encoding='utf-8') as cf:
        cf.write(f'나는 "{filename}"파일입니다, 커피 정보를 담습니다.\n')
# end for

print('각 커피 이름으로 별도 파일 생성')
for coffee in coffees:
    filename = coffee + '.txt'
    with open(file=filename, mode='wt', encoding='utf-8') as cf:
        cf.write(f'{coffee} 정보를 위한 텍스트 파일입니다.\n')
# end for

print('with 구문 사용 예제 - 자동 close()')
with open('coffee_test.txt', mode='wt', encoding='utf-8') as testfile:
    testfile.write('아메리카노\n')
    testfile.write('카페라떼\n')
    testfile.write('모카\n')
    print('오늘의 추천 커피는 아메리카노입니다.', file=testfile)
# end with

print('finished')