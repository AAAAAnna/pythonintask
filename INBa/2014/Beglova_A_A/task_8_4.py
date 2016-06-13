#Задача 8. Вариант 4.
#1-50. Доработайте игру "Анаграммы" (см. М.Доусон Программируем на Python. Гл.4) так, чтобы к каждому слову полагалась подсказка. Игрок должен получать право на подсказку в том случае, если у него нет никаких предположений. Разработайте систему начисления очков, по которой бы игроки, отгадавшие слово без подсказки, получали больше тех, кто запросил подсказку.

# Beglova A. A.
# 13.06.2016

import random
score = 10
words = ("google", "yandex", "chrome", "opera")
word = random.choice(words)
letters = len(word)
print ("Я загадал некоторое слово на английском языке. В нём ", letters, " букв." )
ls = list(word)
random.shuffle(ls)
anagram = ls
i = 0
print(anagram)
answer = ""
while(answer!=word):
	print("Назовёте слово сразу?(Да/Нет)")
	answer = str(input())
	if (answer == str("Да")):
		print("Введите свой ответ: ")
		answer = str(input())
		if (answer == word):
			if (score < 0):
				score == 0
			print("Поздравляю, Вы победили. Ваш счет: ", str(score))
	else:
		print("Хотите взять подсказку(Да/Нет)")
		answer = str(input())
		if (answer == str("Да")):
			print("Подсказка!", i+1, "буква: ", word[i])
			score -= 2
		else:
			print("\nНе очень-то и хотелось...")
			break
input ("\nНажмите Enter для выхода.")
