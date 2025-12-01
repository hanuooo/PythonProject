# 실습 56 페이지
# open() 하면 항상 close() 해주기

print('파일에 기록합니다.')

# .txt 파일을 생성하여 내용을 기록해 봅니다.
filename = 'mem.txt'
myfile01 = open(file=filename, mode='wt', encoding='utf-8')
print(type(myfile01))

# members 리스트의 회원 이름들을 파일로 만들어 봅니다.
members = ['홍영식', '김민수', '박진철', '강호숙']

for mem in members:
    message = f'{mem}님 안녕하세요.\n'
    myfile01.write(message)

myfile01.close()

print(f'{filename}파일이 생성됨')

# .txt 파일에 다른 내용을 덧붙여 추가적으로 더 기록해 봅니다.
print('기존 파일에 내용을 더 추가합니다.')
myfile02 = open(file=filename, mode='at', encoding='utf-8')

for idx in range(len(members)):
    if idx % 2 == 0:
        message = f'{idx}번째 고객 {members[idx]}님 방가워요.\n'
    else:
        message = f'{idx}번째 고객 {members[idx]}님 어서오세요.\n'
    # end if

    myfile02.write(message)
# end for

myfile02.close()

# 반복문을 이용하여 파일을 여러 개(somefile1.txt ~ somefile10.txt) 만들어 봅니다
print('반복문을 사용하여 파일 여러개를 생성합니다.')
print('파일 이름 : somefile01.txt ~ somefile10.txt')

for idx in range(1, 11):
    filename = 'somefile' + str(idx).zfill(2) + '.txt'
    # print(filename)
    myfile = open(file=filename, mode='wt', encoding='utf-8')
    myfile.write(f'나는 {filename}파일 입니다')
    myfile.close()
# end for

print('다음 맴버들의 이름을 사용한 파일을 만들어 보세요.')
members = ['홍영식', '김민수', '박진철', '강호숙']

for mem in members:
    filename = mem + '.txt'
    myfile = open(file=filename, mode='wt', encoding='utf-8')
    myfile.write(mem + ' 고객을 위한 텍스트 파일입니다.\n')
    myfile.close()
# end for

# with ~ as 구문을 이용하여 test.txt 파일을 생성하고 내용을 기록합니다.
# with 사용시 자동 close()
print('with 구문을 사용하면, 암시적으로 close() 함수가 호출 됩니다.')
with open(file='test.txt', mode='wt', encoding='utf-8') as testfile:
    testfile.write('가나다\n')
    testfile.write('abc\n')
    testfile.write('123\n')

    print('hello world', file=testfile)
# end with