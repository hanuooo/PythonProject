human = ['김철수', '홍길동', '박영희']
jumsu = [50, 60, 70]

# for item in zip(human, jumsu):
#     print(item)

mylist = list(zip(human, jumsu))
print(mylist)

mydict = dict(zip(human, jumsu))
print(mydict)

result = sorted(mydict, key=mydict.get, reverse=True)
print(result)