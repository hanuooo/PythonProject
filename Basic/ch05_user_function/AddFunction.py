# 함수의 정의
# 매개 변수 : prarmeter, argument, 인자, 인수라도 부르기도 합니다.
def add(first, second = 15):
    return first + second
# end for

su01 = 14
su02 = 5

# prsitional argument : index를 이용하여 매개 변수에 할당하는 방식
result = add(su01, su02) # 함수의 호출
print('%d + %d = %d ' % (su01, su02, result))

print('%d + %d = %d ' % (100, 200, add(100, 200)))

# keyword argment : 매개 변수 키워드를 이용하여 매개 변수에 할당하는 방식
result = add(second=su01,first=su02)
print('%d + %d = %d'% (su02, su01, result))

# 2방식의 혼합(positional 방식과 keyword 방식이 혼합)
result = add(15 ,second=20)
print('%d + %d = %d'% (15, 20, result))

result = add(10)
print('%d' % result)

