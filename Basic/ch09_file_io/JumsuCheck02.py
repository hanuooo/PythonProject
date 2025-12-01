# jumsu.txt 파일을 읽어 와서 다음의 요구 사항에 만족하는
# result.txt프로그램을 작성해 보세요.
myencoding = 'UTF-8'

# 변수 생성
source = open(file='jumsu.txt', mode='rt', encoding=myencoding) # 읽어올 파일
destination = open(file='result.txt', mode='wt', encoding=myencoding) # 신규 생성 파일

data = [item.strip() for item in source.readlines()]
print(data)

for bean in data:
    # print(type(bean))

    # split() = 문자열을 분리시켜 list 형식으로 만들어 줍니다
    # float() = 실수 타입 변환
    human = bean.split(',')
    # print(human)
    name = human[0]
    kor = float(human[1])
    eng = float(human[2])
    math = float(human[3])
    _gender = human[4].upper() # upper() 대문자화 , lower() 소문자화

    total = kor+eng+math
    average = total/3.0

    if _gender == 'M':
        gender = '남자'
    else:
        gender = '여자'
    # end if

    # 표시 형식 : '이름/성별/총점/평균'
    sentence = '%s/%s/%.1f/%.2f/\n' % (name, gender, total, average)
    print(sentence)
    print(sentence, file=destination)
    destination.write(sentence)
# end for

source.close()
destination.close()

print('처리 작업이 완료 되었습니다.')
