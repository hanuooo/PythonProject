filename = 'test.txt'
myencoding = 'UTF-8'

# readline() = 파일 내에서 1줄을 읽어 들입니다.
# 더 이상 내용이 없으면 None을 리턴해줍니다.
print('readline() 함수는 1줄을 읽어 옵니다.')
myfile01 = open(file=filename, mode='rt', encoding=myencoding)

# \n이 포함된 문자열의 컬렉션의 경우에 줄 단위로 기록이 가능합니다.
while True:
    oneline = myfile01.readline().strip() # 한 줄 읽기,strip() = 문자열 양쪽에 있는 공백 제거
    # print(type(oneline))

    if not oneline: # 마지막 줄에 도달하면 실행됨.
        print(oneline)
        break
    # end if
    print('[' + oneline + ']')
# end while

myfile01.close()

# readlines() = 파일의 모든 내용을 읽어, 각 라인을 요소로 하는 리스트 자료 구조를 만들어 줍니다.
print('readlines() 함수는 모든 줄을 읽어서 list로 반환해 줍니다.')
myfile02 = open(file=filename, mode='rt', encoding=myencoding)
sentences = [txt.strip() for txt in myfile02.readlines()]
# print(type(sentences))
print(sentences)

myfile02.close()

# 파일의 내용 전체를 문자열로 반환합니다.
# read(정수)를 이용하면 정수만큼의 바이트를 읽어 옵니다.
print('read() 함수는 파일 내용 전체를 문자열로 반환해 줍니다.')
myfile03 = open(file=filename, mode='rt', encoding=myencoding)

sentences = myfile03.read()

print(type(sentences))
print(sentences)

myfile03.close()