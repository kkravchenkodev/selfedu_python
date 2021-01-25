"""
Анаграмма
Cтрока S1 называется анаграммой строки S2, если она получается из S2 перестановкой символов.
Программа получает на вход две строки S1 и S2.
Если строка S1 является анаграммой строки S2 нужно вывести YES, в противном случае - NO
"""
# s1 = input()
# s2 = input()
# count1 = {}
# count2 = {}
#
# for character in s1:
#     count1.setdefault(character, 0)
#     count1[character] = count1[character] + 1
# for character in s2:
#     count2.setdefault(character, 0)
#     count2[character] = count2[character] + 1
# if count2 == count1:
#     print('YES')
# else:
#     print('NO')

print('YES' if sorted(input()) == sorted(input()) else 'NO')
