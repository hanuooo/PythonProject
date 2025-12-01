# def add(sayHello01, sayHello02):
#     return sayHello01 + sayHello02
# # end def
#
# sayHello01 = '안녕하세요'
# sayHello02 = '방가워요'
#
#
# result = add(sayHello01, sayHello02)
#
# print('%s\n' % sayHello01 * 5)
# print('\n')
# print('%s\n' % sayHello02 * 7)

def sayHello(message, n=10):
    for i in range(n):
        print(message)
    print()

sayHello('안녕하세요.',5)

sayHello(message = 'hello', n = 7)

sayHello(n =3 , message = '곤니찌와')

sayHello('방가워요') # 반복 횟수에 기본값이 있습니다.