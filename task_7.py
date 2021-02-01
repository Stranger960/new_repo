
### item 7
############# не уверен, что правильно понял само задание... 

def fact(k):                         #  подсчет факториала k!
    rslt = 1
    for cnt in range(1, k + 1):
        rslt *= cnt
    yield rslt

for n in range(100):
    for rslt in fact(n):             #  обращение к генератору
        if rslt <= n:                #  вывод n первых значений
            print(rslt)