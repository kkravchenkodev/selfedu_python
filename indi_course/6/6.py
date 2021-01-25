"""
Представьте, у нас есть список товаров и их стоимость, но мы хотим взглянуть на него в отсортированном виде. Вверху хотим видеть самые дорогие товары, внизу самые дешевые
Программа будет принимать строки, в которых сперва указывается название товара, а затем через двоеточие с пробелом его цена - целое положительное число.
Строка "конец" означает списка товаров и соответственно окончание ввода
Все товары имеют уникальные названия, цены не дублируются.
Ваша задача вывести список товаров по уменьшению цены

Sample Input:
Sony PlayStation 5: 46000
Телевизор QLED Samsung QE65Q60TAU: 87090
Смартфон Samsung Galaxy A11: 10000
Планшет Samsung Galaxy Tab S6: 26600
конец

Sample Output:
Телевизор QLED Samsung QE65Q60TAU
Sony PlayStation 5
Планшет Samsung Galaxy Tab S6
Смартфон Samsung Galaxy A11
"""
dct = {}
while True:
    inpt = input()
    if inpt == 'конец':
        break
    inpt = inpt.split(':')
    dct[inpt[0]] = int(inpt[1])

for i in sorted(dct.items(), key=lambda pair: pair[1], reverse=True):
    print(i[0])
