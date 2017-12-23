# Задание 3
# Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика

is_male = {
  'Оля': False,  # если True, то пол мужской
  'Петя': True,
  'Вася': True,
  'Маша': False,
}
names = ['Оля', 'Петя', 'Вася', 'Маша']

for name in range(len(names)):
    str_name = (names[name])
    if str(is_male[str(str_name)]) == 'True':
        print(str(str_name) + ' male') 
    else: 
        print(str(str_name) + ' female')

