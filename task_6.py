### item 6
#p1
from itertools import count
from sys import argv
s_name, start, finish = argv  # распаковка
start, finish = int(start), int(finish)
for itr in count(start):
    if itr > finish:
        print(f"\nHave a nice day !")
        break
    else:
        print(f"Count => {itr:2d}")


#p2		
#run => python script1.py 7
from itertools import cycle
from sys import argv

s_name, finish = argv  # распаковка
finish = int(finish)
itr = 0
for line in cycle(("Жизнь хороша", "Проживи неспеша")):
    if itr > finish+1:
        break
    print(line,"...")
    itr += 1  