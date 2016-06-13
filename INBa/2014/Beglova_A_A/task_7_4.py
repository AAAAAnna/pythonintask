# Задача 7. Вариант 4.
# 1-50. Разработайте систему начисления очков для задачи 6, в соответствии с которой игрок получал бы большее количество баллов за меньшее количество попыток.

# Beglova A. A.
# 13.06.2016

import random

print("Компьютер загадал название одного из шести континентов Земли, а Вы должны его угадать.\n")

podvigs = ('Немейский лев','Лернейская гидра','Стимфалийские птицы','Керинейская лань','Эриманфский вепрь','Авгиевы конюшни','Критский бык','Кони Диомеда','Пояс Ипполиты','Стадо Гериона','Яблоки Гесперид','Укрощение Цербера')
pp = random.randint(0,11)
x = 0
i = 0
score = 0


while(x != 11):
	print(podvigs[x])
	x += 1

answer = input("\nВведите название подвига: ")

while(answer != podvigs[pp]):
    print("Неверно, попробуйте ещё раз.")
    answer = input("\nВведите название подвига: ")
    i += 1

if i == 0:
	score = 10
	
elif 0<i<6:
	score = 10 - i*2
	
else:
	score = 0

print("Верно, Вы победили!")
print("Число попыток: "+str(i))
print("Вы заработали "+str(score)+" баллов")

input("\nДля выхода нажмите Enter.")