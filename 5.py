# Задание 5
# Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят.
# Пример:
# Группа 1: Вася, Маша
# Группа 2: Оля, Петя, Гриша

groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]

#РЕШЕНИЕ 1

numb_slice = 0
number_group = 0

for group_name in groups:
    number_group += 1
    print('Группа %s : %s' % ((number_group), (', '.join(groups[numb_slice]))))
    numb_slice += 1


#РЕШЕНИЕ 2

# for group_name in range(len(groups)):
#     print(len(groups))
#     number_group = len(groups[group_name])
#     print('Группа %s : %s' % ((number_group), (', '.join(groups[group_name]))))