"""
Напишите функцию longest_word_in_file, которая принимает имя файла и внутри его содержимого находит самое длинное слово
и возвращает его в качестве ответа. В случае,  если есть несколько слов с максимальной длиной, нужно вернуть слово,
которое встречается последнее в тексте.
При этом слова в тексте отделяются друг от друга пробелами, любые другие знаки пунктуации необходимо исключить.
И также учитывайте, что слова в тестах будут как на русском языке, так и на английском

Все возможные знаки пунктуации можно получить из модуля string
from string import punctuation
"""


def longest_word_in_file(file_name):
    # def remove_punctuation(w):
    #     for p in punctuation:
    #         if p in w:
    #             w = w.replace(p, "")
    #     return w
    #
    with open(file_name, 'r', encoding='utf-8') as file:
        from string import punctuation
    # #     words = [remove_punctuation(word) for word in file.read().split()]
    # #     max_length = max(list(map(len, words)))
    # #     return list(filter(lambda word: len(word) == max_length, words))[-1]
        text = [i.strip() for i in file.read().split()]
        data_lst = [word.strip(punctuation) for word in text]
        return sorted(data_lst, key=len)[-1]
    #
    # from re import split
    # with open(file_name, 'r', encoding='utf-8') as f:
    #     return max(split('\W+', f.read())[:: -1], key=lambda x: len(x))


print(longest_word_in_file('test'))
