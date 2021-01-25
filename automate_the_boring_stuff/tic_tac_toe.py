from pprint import pprint

the_board = {'top-L': 'X', 'top-M': ' ', 'top-R': 'O', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ',
             'low-M': ' ', 'low-R': ' ', }

pprint(the_board, indent=2)


def print_board(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


print_board(the_board)