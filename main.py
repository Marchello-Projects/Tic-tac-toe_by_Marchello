from colorama import Fore, init
import random

init(autoreset=True) 

board = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]

combinations_first_player = []
combinations_second_player = []

horizontal_winning_combinations = [
    (0, 0),
    (0, 1),
    (0, 2),
    (1, 0),
    (1, 1),
    (1, 2),
    (2, 0),
    (2, 1),
    (2, 2)
]

vertical_winning_combinations = [
    (0, 0),
    (1, 0),
    (2, 0),
    (0, 1),
    (1, 1),
    (2, 1),
    (0, 2),
    (1, 2),
    (2, 2)
]

game_is_run = True
game_over = False

symbol = 'X'

first_player = input('Please enter the first player\'s nickname: ')
second_player = input('Please enter the second player\'s nickname: ')

player_now = first_player

while game_is_run:
    if first_player == '' or second_player == '':
        print('The parameters entered are empty. Try again')
        break

    for row in board:
        for cell in row:
            if cell == 'X':
                print(Fore.RED + cell, end=' ')
            elif cell == 'O':
                print(Fore.BLUE + cell, end=' ')
            else:
                print(cell, end=' ')
        print()

    select_row=input(f'{player_now} enter row (index starts from 0 and ends at 2): ')
    select_cell=input(f'{player_now} enter cell (index starts from 0 and ends at 2): ')

    if not select_row or not select_cell:
        print('The parameters entered are empty. Try again')

    select_row = int(select_row)
    select_cell = int(select_cell)

    if select_row > 2 or select_cell > 2:
        print('Value is greater than index. Try again')

    if select_row < 0 or select_cell < 0:
        print('Value is less than index. Try again')

    board[select_row][select_cell] = symbol

    if symbol == 'X':
        symbol = 'O'
    elif symbol == 'O':
        symbol = 'X'

    if player_now == first_player:
        combinations_first_player.append((select_row, select_cell))
        player_now = second_player
    elif player_now == second_player:
        combinations_second_player.append((select_row, select_cell))
        player_now = first_player