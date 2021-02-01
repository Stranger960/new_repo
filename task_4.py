### item 4

lst = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new =[]
res = [ new.append(k) for k in lst if k not in new ]
print ("Initial  list: ", lst,"\nUnique values: ", new)
