myencoding = 'UTF-8'

source = open(file='coffee.txt', mode='rt', encoding=myencoding)
destination = open(file='coffee_result.txt', mode='wt', encoding=myencoding)

print('coffee.txt 파일 내용')
mycoffee01 = open(file='coffee.txt', mode='rt', encoding=myencoding)

sentence01 = mycoffee01.read()

print(sentence01)

mycoffee01.close()

data = [item.strip() for item in source]

print('coffee_result.txt 파일 내용')

discounts = {
    "아메리카노":0.90,
    "라떼":0.95,
    "카푸치노":0.93,
    "바닐라라떼":0.92,
    "모카":0.94
}

for bean in data:
    coffee = bean.split(',')
    name = coffee[0]
    price = int(coffee[1])
    quantity = int(coffee[2])

    total = int(price*quantity*discounts[name]) # 할인 계산

    # 결과 출력
    print(f'{name}/{price}/{quantity}/{total}')
destination.close()
source.close()
