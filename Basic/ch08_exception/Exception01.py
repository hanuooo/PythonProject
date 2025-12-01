try:
    x, y = 4, 2

    z = x / y
    print(z)

    mylist = [1, 2, 3]
    print(mylist[1])

    dict_fruit = {'사과':10, '바나나':20}
    print(dict_fruit['오렌지'])

    print('예외가 발생하면 이 부분은 실행이 되지 않습니다.')

except ZeroDivisionError as err:
    print('0으로 나누시면 안됩니다.')
    print('예외 객체 정보 : %s' % err)

except IndexError as err:
    print('인덱스의 접근 범위를 벗어남.')
    print('예외 객체 정보 : %s' % err)

except Exception as err:
    print('기타 나머지 예외 발생.')
    print('예외 객체 정보 : %s' % err)

else:
    print('예외가 발생하지 않으면 나는 실행이 됩니다.')

finally:
    print('예외 발생 여부와 상관없이 무조건 실행이 됩니다.')
# end try