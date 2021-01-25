with open('numbers.txt', 'r', encoding='utf-8') as input_file:
    payload = [i.strip('\n') for i in input_file.readlines()]
    count = len(list(filter(lambda x: len(x) == 3, payload)))
    summa = sum(list(map(int, list(filter(lambda x: len(x) == 2, payload)))))
    print(f'{count},{summa}')
