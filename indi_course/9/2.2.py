"""
К вам в руки попал файлик формата json (manager_sales.json), в котором содержится информация одного автосалона о продажах менеджеров.
В файле указано для каждого менеджера список проданных им автомобилей,
а также проставлена цена продажи каждого автомобиля.
Ваша задача скачать файлик и самостоятельно найти имя и фамилию самого успешно менеджера, а также общую сумму его продаж.
В качестве ответа нужно через пробел указать сперва его имя, затем фамилию и после общую сумму его продаж.
"""
import json

with open('manager_sales.json') as file:
    data = json.load(file)
dct = {}
for each in data:
    name = f"{each['manager']['first_name']} {each['manager']['last_name']}"
    total = sum([i['price'] for i in each['cars']])
    dct[name] = total
print(sorted(dct.items(), key=lambda x: -x[1])[0])
