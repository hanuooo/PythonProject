mylist = [10, -20, 30, -40, 50]

newmylist = [abs(x) for x in mylist]
print(sum(newmylist))
print('-'*30)
print(newmylist)
print(sum(newmylist))

# total = 0
# for item in mylist:
#     if item < 0 :
#         item = abs(item)
#     total += item
#
# print(total)
# print('-'*30)
# for idx in range(len(mylist)):
#     if mylist[idx] < 0:
#         mylist[idx] = abs(mylist[idx])
#
# print(mylist)
# print(sum(mylist))
# print('-'*30)
