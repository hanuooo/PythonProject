breadListString = "바게트,크로와상,스콘,치아바타,나쵸,식빵,스콘,호밀빵,베이글"
breadList = breadListString.split(",")

print(type(breadList))
print('원본 데이터')
print(breadList)

newBread = breadList[0:3]
newBread.append(breadList[1])
print('새로운 데이터')
print(newBread)
#Re00

