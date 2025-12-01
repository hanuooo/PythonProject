coffees = ['바닐라라떼', '카페라떼', '고구마라떼']
price = [1000, 2000, 3000]

# zip()
for item in zip(coffees, price):
    print(item)
# end for

mylist = list(zip(coffees, price))
print(mylist)

mydict = dict(mylist)
print(mydict)

# sorted()
print('key를 사용한 오름차순 정렬')
result = sorted(mydict.keys())
print(result)

print('key를 사용한 내림차순 정렬')
result = sorted(mydict.keys(), reverse=True)
print(result)

print('value를 사용한 오름차순 정렬')
result = sorted(mydict.values())
print(result)

print('value를 사용한 내림차순 정렬')
result = sorted(mydict.values(), reverse=True)
print(result)

print('value를 기준으로 내림차순 정렬하되, 품목 이름 출력')
result = sorted(mydict, key=mydict.get, reverse=True) # 품목이름이아닌 키 값의 수치로 정렬
print(result)
