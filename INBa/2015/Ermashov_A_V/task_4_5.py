#Напишите программу, которая выводит имя, под которым скрывается Фредерик Аустерлиц. 
#Дополнительно необходимо вывести область интересов указанной личности, место рождения, 
#годы рождения и смерти (если человек умер), вычислить возраст на данный момент (или момент смерти). 
#Для хранения всех необходимых данных требуется использовать переменные. После вывода информации программа должна
#дожидаться пока пользователь нажмет Enter для выхода.
# Ермашов А.В.,28.03.2016

name = "Фредерик Аустерлиц"
birthplace = "Омахе, штат Небраска"
birthyear = int (1899)
deathyear = int (1987)
age = int (deathyear - birthyear)
interest = "Актёр,певец"
print(name+" наиболее известен как Фред Астер - американский актёр,\nтанцор,хореограф и певец,звезда Голливуда.")
print("Место рождения: "+birthplace)
print("Год рождения: "+str(birthyear))
print("Год смерти: "+str(deathyear))
print("Возраст смерти: "+str(age))
print("Область интересов: "+interest)
input("\nДля выхода нажмите Enter") 
