"""
Премия Оскар
Представьте, что мы с вами сами можем решать кому и сколько статуэток Оскара уйдет (Лео бы тогда давно купался в этих статуэтках)
Ваша задача написать программу, которая находит информацию, кто из актеров получил наибольшее и наименьшее количество статуэток
Входные данные
Программа принимать на вход в первой строке натуральное число n - количество вручаемых сегодня наград. И затем в n следующих строках вводятся имена актеров - победителей.
Выходные данные
Нужно вывести в  отдельных строках имена актеров набравших наибольшее и наименьшее количество статуэток и через запятую их количество. Гарантируется, что всегда будет только один человек, набравших наибольшее и наименьшее количество статуэток.

Sample Input:
6
Леонардо Ди Каприо
Джонни Депп
Леонардо Ди Каприо
Леонардо Ди Каприо
Джонни Депп
Мэтт Деймон

Sample Output:
Леонардо Ди Каприо, 3
Мэтт Деймон, 1
"""

actors = [input() for _ in range(int(input()))]
dct = {each: actors.count(each) for each in actors}
lst = sorted(dct.items(), key=lambda x: x[1], reverse=True)
print(*lst[0], sep=',')
print(*lst[-1], sep=',')