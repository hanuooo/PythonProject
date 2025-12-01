class MinjumsuException(Exception):
    def __init__(self, message):
        super().__init__(message)
# end class MinjumsuException
class FailedException(Exception):
    def __init__(self, message):
        super().__init__(message)
# end class FailException

try:
    name = input('이름을 입력해 주세요.')
    kor = int(input('국어 점수 : '))
    eng = int(input('영어 점수 : '))
    math = int(input('수학 점수 : '))

    if kor < 40 or eng < 40 or math < 40:
        msg = '%s 님 과락입니다.' % name
        # 객체 생성 후 raise 실행
        raise MinjumsuException(msg)

    average = (kor + eng + math) / 3.0
    if average < 60.0:
        msg = '%s님 불합격입니다.' % name
        raise FailedException(msg)

    print('%s님 합격입니다.' % name)

except MinjumsuException as err:
    print('시험을 잘 못 보셨군요.')
    print(err)
except FailedException as err:
    print('조금만 더 공부하시길 바랍니다.')
    print(err)
except Exception as err:
    print('기타 예외 발생.')
    print(err)
# end try