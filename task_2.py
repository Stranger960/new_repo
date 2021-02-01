### item 2

lst = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
lst_out = [ lst[j] for j in range(1,len(lst)) if lst[j] > lst[j-1]  ]
print("\n Ввводим список: ",lst)
print(" Результат: ",lst_out)