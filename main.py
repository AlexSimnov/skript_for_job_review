# Подключение библиотеки для чтени .xls файлов
import xlrd as op
import pprint as pp
from collections import OrderedDict

# Подкл библиотеки для поиска директории
import os

#место папки
loc = '/Users/aleksejsimonov/Desktop/skript_for_job_review/skript_for_job_review'

# переменная где нахожусь
content = os.listdir(loc)

# Переменная с имененем файла
filename = ''

for file in content:
    if len(file) > 20:
        filename = file
    break
        

car_dict = {}

# key = rus
ang_word = {'А':'A', 'В':'B', 'Е':'E', 'К':'K', 'М':'M', 'Н':'H', 'О':'O', 'Р':'P', 
            'С':'C', 'Т':'T', 'У':'Y', 'Х':'X'}


# Открытие файла
wb = op.open_workbook(filename)

# работа с 1 стр
sheet = wb.sheet_by_index(0)

# Максимальное значение в колонке
max_rows = sheet.nrows



#Перебор ячеек с машинами и что сделанно

for i in range(5, max_rows):
    for j in range(4, 5):
        # переменная время когда сделал машину
        time = sheet.cell_value(i, j+1)
        # костыли чтобы если меньше 2х симвл выводился
        time = time[11:16]
        if time.startswith('9:'):
            time = '09:00'
        elif time.startswith('8:'):
            time = '08:00'

        # переменная во сколько + номер тс
        car = time + ' ' + sheet.cell_value(i, j)
        
        # перебрать все буквы и заменить на англ раскладку
        rcar = ''
        for word in car:
            if word in ang_word:
                rcar += ang_word[word]
            elif word not in ang_word:
                rcar += word
        car = rcar

        #  переменная сделанная работа
        work = sheet.cell_value(i, j+2) + ' ' + str(sheet.cell_value(i, j+3))
            # если ранее не вст ключ(машину) создается новая пара
        if car not in car_dict:
            # создаем пару ключ(машина) = значению(list[работа])
            car_dict[car] = [work]
        else:
            # встр машину второй раз
            car_dict[car].append(work)
        
        


# сортировка файла от самого мал к бол
dict = OrderedDict(sorted(car_dict.items(), key=lambda t: t[0]))
    



with open('rabi.ini', 'w') as myfile:
    for key, value in dict.items():
        string_values =  '\n'.join(value)
        string_to_write = key + ' : \n' + string_values + '\n'
        myfile.write(string_to_write)
        myfile.write('\n')
