"""
Имеется набор оценок в виде строки:
    "Оценки: 5,4,3,2,5,3,2,4"
Необходимо создать кортеж, в котором находились бы только оценки в виде целых чисел:
    (5,4,3,2,5,3,2,4)
"""
marks = "Оценки: 5,4,3,2,5,3,2,4  "
print(tuple(marks.replace("Оценки:", "").strip().split(',')))
