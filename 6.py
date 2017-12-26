# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

list_name = []
count_name = 0
for students_name in students:
    name = students_name['first_name']
    if name not in list_name:
        list_name.append(students_name['first_name'])
#     if name in list_name:
#         count_name += 1
# print(count_name)
print(list_name)



