# Задание 2
# Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём.

names = ['Оля', 'Петя', 'Вася', 'Маша']
for name in range(len(names)):
    count_symb = len(names[name])
    one_name =(names[name])
    print(str(one_name) + ' Количество букв ' + str(count_symb) )