import pprint as pp

telega_rew = open('telgram_rev.txt', 'r')

gost = {'Нестандартная': 'Нестандартная операция', 'Перезагрузка телематики': 'Перезагрузка оборудования',
        'Зарядка АКБ': 'Зарядка АКБ', '': ''}

car_dict = {}
work = str

car = str

# читает файл по строке
for i in telega_rew.readlines():

    # начинается стр с датой
    if i.startswith('Алексей'):

        # читает по слову 
        for y in i.split(' '):
            # убирает все кроме времени 
            if y[2:3] == ':':
               y[:5]

    # поиск тс
    if len(i) == 10:

        # переменная с временем и номером тс
        car = y[:5] + ' ' + i[:-1] + ' : '

    # проверка только сделанная работа
    if i == '\n':
        continue
    if  i != car and len(i) != 10 and not i.startswith('Алексей'):
        work = i[:-1]
    
    
    if car not in car_dict:
            # создаем пару ключ(машина) = значению(list[работа])
            car_dict[car] = [work]
    else:
        # встр машину второй раз
        car_dict[car].append(work)



with open('telga.ini', 'w') as myfile:
    for key, value in car_dict.items():
        # вывод только val словаря
        string_values =  ' '.join(map(str, car_dict[key])) + '\n' 
        string_to_write = str(key)  + '\n' + str(string_values)
        myfile.write(string_to_write)
        myfile.write('\n')
