# Задание 4
# Даны группа учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней
# Пример вывода:
# Всего 2 группы.
# В группе 2 ученика.
# В группе 3 ученика.

groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]
print('Всего ' + str(len(groups)) + ' группы:')

for group in range(len(groups)):
    print('В группе ' + str(len(groups[group])) + ' ученика')
    #print(str(groups[0]))