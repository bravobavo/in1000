'''ASSIGNMENT 1'''
#1
myList = [3,5,9]
myList.append(8)
print(myList,'\nValue 1: {0}\nValue 2: {1}'.format(myList[0],myList[2]))
#2
newList = [input("Name, please: ") for _ in range(0,4)]
#3
if "Bavo" in newList: print('Our impressive if-statement found Bavo!')
else: print('No Bavo here...')
#4
twoLists = myList + newList
print(twoLists)
twoLists[-2:] = []
print(twoLists)
