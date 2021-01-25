n = int(input())


def create_file_with_numbers(n):
    file_name = f'range_{n}.txt'
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, n + 1):
            file.write(str(i) + '\n')


create_file_with_numbers(n)
