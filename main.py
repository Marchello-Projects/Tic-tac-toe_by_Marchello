from colorama import Fore, Style, init
from openpyxl import Workbook

init(autoreset=True)
wb = Workbook()

board = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]

combinations_first_player = [[]]
combinations_second_player = [[]]

horizontal_winning_combinations = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)]
]

vertical_winning_combinations = [
    [(0, 0), (1, 0), (2, 0)], 
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)]
]

diagonal_winning_combinations = [
    [(0, 0), (1, 1), (2, 2)], 
    [(0, 2), (1, 1), (2, 0)],
]

game_is_run = True

symbol = 'X'

first_player = input('Please enter the first player\'s nickname: ')
second_player = input('Please enter the second player\'s nickname: ')

player_now = first_player

while game_is_run:
    if not first_player or not second_player:
        print('The parameters entered are empty. Try again')
        break

    for row in board:
        print("+---" * len(row) + "+")  
        print("|", end="")  
        for cell in row:
            if cell == 'X':
                print(f" {Fore.RED}{cell}{Style.RESET_ALL} |", end="")  
            elif cell == 'O':
                print(f" {Fore.BLUE}{cell}{Style.RESET_ALL} |", end="")  
            else:
                print("   |", end="")  
        print()  
    print("+---" * len(board[0]) + "+")  


    select_row=input(f'{player_now}, enter row (index starts from 0 and ends at 2): ')
    select_cell=input(f'{player_now}, enter cell (index starts from 0 and ends at 2): ')

    if not select_row or not select_cell:
        print('The parameters entered are empty. Try again')

    select_row = int(select_row)
    select_cell = int(select_cell)

    if select_row > 2 or select_cell > 2:
        print('Value is greater than index. Try again')

    if select_row < 0 or select_cell < 0:
        print('Value is less than index. Try again')

    if board[select_row][select_cell] != '':
        print('Cell is not empty. Try again')
        game_is_run = False


    board[select_row][select_cell] = symbol

    if symbol == 'X':
        symbol = 'O'
    elif symbol == 'O':
        symbol = 'X'

    if player_now == first_player:
        combinations_first_player[0].append((select_row, select_cell))
        
        for _, combination_first_player in enumerate(combinations_first_player):
            for _, combination_vertical in enumerate(vertical_winning_combinations):
                if combination_first_player == combination_vertical:
                    game_is_run = False

                    print(f'{Fore.GREEN}{player_now} Wins!{Style.RESET_ALL}')

                    sheet = wb.active
                    sheet.title = 'Statistics'
                    
                    sheet["A1"] = f'Winner'
                    sheet["B1"] = f'Loser'
                    sheet["A2"] = f'{first_player}'
                    sheet["B2"] = f'{second_player}'
                    
                    wb.save("Statistics.xlsx")

        for _, combination_first_player in enumerate(combinations_first_player):
            for _, combination_horizontal in enumerate(horizontal_winning_combinations):
                if combination_first_player == combination_horizontal:
                    game_is_run = False

                    print(f'{Fore.GREEN}{player_now} Wins!{Style.RESET_ALL}')

                    sheet = wb.active
                    sheet.title = 'Statistics'
                    
                    sheet["A1"] = f'Winner'
                    sheet["B1"] = f'Loser'
                    sheet["A2"] = f'{first_player}'
                    sheet["B2"] = f'{second_player}'
                    
                    wb.save("Statistics.xlsx")

        for _, combination_first_player in enumerate(combinations_first_player):
            for _, combination_diagonal in enumerate(diagonal_winning_combinations):
                if combination_first_player == combination_diagonal:
                    game_is_run = False

                    print(f'{Fore.GREEN}{player_now} Wins!{Style.RESET_ALL}')

                    sheet = wb.active
                    sheet.title = 'Statistics'
                    
                    sheet["A1"] = f'Winner'
                    sheet["B1"] = f'Loser'
                    sheet["A2"] = f'{first_player}'
                    sheet["B2"] = f'{second_player}'
                    
                    wb.save("Statistics.xlsx")
        
        if all(cell != '' for row in board for cell in row):
                    game_is_run = False

                    print(f'{Fore.YELLOW}It\'s a draw!{Style.RESET_ALL}')

        player_now = second_player
    elif player_now == second_player:
        combinations_second_player[0].append((select_row, select_cell))

        for _, combination_second_player in enumerate(combinations_second_player):
            for _, combination_vertical in enumerate(vertical_winning_combinations):
                if combination_second_player == combination_vertical:
                    game_is_run = False

                    print(f'{Fore.GREEN}{player_now} Wins!{Style.RESET_ALL}')

                    sheet = wb.active
                    sheet.title = 'Statistics'
                    
                    sheet["A1"] = f'Winner'
                    sheet["B1"] = f'Loser'
                    sheet["A2"] = f'{second_player}'
                    sheet["B2"] = f'{first_player}'
                    
                    wb.save("Statistics.xlsx")

        for _, combination_second_player in enumerate(combinations_second_player):
            for _, combination_horizontal in enumerate(horizontal_winning_combinations):
                if combination_second_player == combination_horizontal:
                    game_is_run = False

                    print(f'{Fore.GREEN}{player_now} Wins!{Style.RESET_ALL}')

                    sheet = wb.active
                    sheet.title = 'Statistics'
                    
                    sheet["A1"] = f'Winner'
                    sheet["B1"] = f'Loser'
                    sheet["A2"] = f'{second_player}'
                    sheet["B2"] = f'{first_player}'
                    
                    wb.save("Statistics.xlsx")

        for _, combination_second_player in enumerate(combinations_second_player):
            for _, combination_diagonal in enumerate(diagonal_winning_combinations):
                if combination_second_player == combination_diagonal:
                    game_is_run = False

                    print(f'{Fore.GREEN}{player_now} Wins!{Style.RESET_ALL}')  

                    sheet = wb.active
                    sheet.title = 'Statistics'
                    
                    sheet["A1"] = f'Winner'
                    sheet["B1"] = f'Loser'
                    sheet["A2"] = f'{second_player}'
                    sheet["B2"] = f'{first_player}'
                    
                    wb.save("Statistics.xlsx") 

        player_now = first_player