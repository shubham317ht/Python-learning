# list is mutable and values of the list can be changed

list = ['shubham goenka', 90, 'hinjewadi phase-1', 'pune']  # syntax of list
list2 = ['cdac', 'akurdi']
listNum = [1, 2, 3, 6, 4, 5]
listAlpha = ['b', 'a', 'c', 1]
print(list)
print(list[1:])
list.append('bike')
list.append(['bike2'])
list.append(list2)
print(list)
list3 = list.copy()  # seperate copy of list created
list3.append(['bag'])
list3.extend(list)
print(list)
print(list3)
print(listAlpha)
sorted(listNum)  # list can be sorted only homogenous elements are present
# listAlpha.sort() # list can't be sorted list is heterogenous
print(sorted(listNum))  # returns the new copy of sorted list
listNum.sort()  # sort the same list
print(listNum)
print(list.count('shubham goenka'))  # count exact match with the element
