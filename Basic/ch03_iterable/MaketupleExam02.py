breadListString = "바게트,크로와상,스콘,치아바타,나쵸,식빵,스콘,호밀빵,베이글"
breadList = breadListString.split(",")

breadTuple = tuple(breadList)
print("원본 튜플:", breadTuple)

print("스콘 개수:", breadTuple.count("스콘"))
print("스콘 첫 번째 인덱스:", breadTuple.index("스콘"))

tuple01 = breadTuple[:3]
tuple02 = breadTuple[-3:]

newTuple = tuple01 + tuple02
print("새로운 튜플:", newTuple)

newList = list(newTuple)
print('오름차순 정렬')
newList.sort()
print(newList)
# Re00