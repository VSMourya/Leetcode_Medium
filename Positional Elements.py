

ls = [[1,3,4],
      [5,2,9],
      [8,7,6]]

deleteList = []


store = []

for i in range(len(ls)):
    deleteList.append(min(ls[i]))

for i in range(len(ls)):
    deleteList.append(max(ls[i]))

for i in range(len(ls)) :
    for j in ls[i] :
        store.append(j)

print(set(store) - set(deleteList))









