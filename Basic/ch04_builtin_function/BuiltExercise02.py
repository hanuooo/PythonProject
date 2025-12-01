human = ['김철수', '홍길동', '박영희', '심수련', '유재민']

mylist = [name for index, name in enumerate(human) if index % 2 == 0]
print(mylist)

newhuman = [name + '님' for index, name in enumerate(human) if index % 2 == 0]
print(newhuman)

# mylist = []
# for idx, value in enumerate(human):
#     if idx % 2 == 0:
#         mylist.append(value)
# print(mylist)
#
# newhuman = list(item + '님' for item in human)
# print(newhuman)