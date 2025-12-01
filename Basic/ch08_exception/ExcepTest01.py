try:
    su1 = 10
    su2 = '20'

    result = su1 + su2
    print(result)

    mydict = {'hong': 10, 'kim': 20}
    findKey = 'choi'
    print(mydict[findKey])

    print('예외가 발생하지 않았으므로, 이 부분은 실행이 됩니다.')

except TypeError as err:
    print('지원하지 않는 연산 방식입니다.')
    print('예외 객체 정보 : %s' % err)

except KeyError as err:
    print('사전에 찾고자 하는 키 정보가 존재하지 않습니다.')
    print('예외 객체 정보 : %s' % err)

except Exception as err:
    print('기타 나머지 예외 발생.')
    print('예외 객체 정보 : %s' % err)

else:
    print('예외가 발생하지 않으면 나는 실행이 됩니다.')

finally:
    print('예외 발생 여부와 상관 없이 무조건 실행이 됩니다.')

