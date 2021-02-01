### item 1
"""
модель / проверка - получаем кортеж: argv = ("script", "160", "500", "5000")
результат - зарплата 85000
запуск:
D:\>python script1.py 160 500 5000
"""

from sys import argv

s_name, work_h, pay_per_h, bonus = argv  # распаковка
salary = (int(work_h) * int(pay_per_h) + int(bonus))

print("\nИмя скрипта: ", s_name)
print("Введены следующие параметры:")
print("выработка в часах => ", work_h)
print("ставка в час => ", pay_per_h)
print("премия => ", bonus)
print(f"\nЗаработная плата сотрудника составит: {salary}  руб")