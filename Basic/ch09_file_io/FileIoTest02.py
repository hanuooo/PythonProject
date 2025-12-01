filename = 'coffee_list.txt'
myencoding = 'UTF-8'

print('# readline() 함수 사용')
myfile01 = open(file=filename, mode='rt', encoding=myencoding)

while True:
    oneline = myfile01.readline()

    if not oneline:
        print(oneline)
        break
    # end if
    print(oneline)
# end while
myfile01.close()

print('# readlines() 함수 사용')
myfile02 = open(file=filename, mode='rt', encoding=myencoding)
sentence = [txt.strip() for txt in myfile02.readlines()]
print(sentence)

myfile02.close()

print('')

print('# read() 함수 사용')
myfile03 = open(file=filename, mode='rt', encoding=myencoding)

sentence = myfile03.read()

print(sentence)

myfile03.close()

print('')
print('finished')