# Задача 5. Вариант 4.
# Напишите программу, которая бы при запуске случайным образом отображала один из трех цветов светофора.

# Beglova A. A.
# 13.06.2016

import random

print ("Напишите программу, которая бы при запуске случайным образом отображала один из трех цветов светофора.")

x = int (random.randint(1,3))

print ('\nЦвет - ')

if x == 1:
    print ('Красный')
elif x == 2:
    print ('Желтый')
else:
    print ('Зеленый')
    
input("\nДля выхода нажмите Enter.")
