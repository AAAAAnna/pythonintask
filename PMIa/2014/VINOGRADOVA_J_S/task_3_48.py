# Задача 3. Вариант 48.
# Напишите программу, которая выводит имя "Борис Николаевич Кампов", и запрашивает его псевдоним. Программа должна сцеплять две эти строки и выводить полученную строку, разделяя имя и псевдоним с помощью тире.

# Vinogradova J. 
# 31.03.2016

name = "Борис Николаевич Кампов"
print("Герой нашей сегоднящней программы - " + name)
alias = input("Под каким же именем мы знаем этого человека? Ваш ответ: ")

print("Все верно: " + name + " - " + alias)

input("\n\nНажмите Enter для выхода.")