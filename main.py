from colorama import Fore, Style, init
from openpyxl import Workbook
import random

init(autoreset=True)
statistics = Workbook()

board = [
    ['', '', ''], 
    ['', '', ''], 
    ['', '', '']
]

winning_combinations = [
    [(0, 0), (0, 1), (0, 2)], 
    [(1, 0), (1, 1), (1, 2)], 
    [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)], 
    [(0, 1), (1, 1), (2, 1)], 
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)], 
    [(0, 2), (1, 1), (2, 0)]
]

def check_win(player_moves):
    for win_combination in winning_combinations:
        if all(pos in player_moves for pos in win_combination):
            return True
    return False

game_is_run = True
select_mode = input('Please, select game mode (1. Against a bot, 2. Against each other): ')

if select_mode != '1' and select_mode != '2':
    print('Try again')

if select_mode == '1':
    nick_name = input('Please enter your nick-name: ')
    bot = 'Bot'

    total_player_wins = 0
    total_bot_wins = 0

    player_symbol = 'X'
    bot_symbol = 'O'

    player_combinations = []
    bot_combinations = []

    if not nick_name:
        print('The nick-name entered is empty. Try again')

    player_now = nick_name

    while game_is_run:
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

        select_row = input(f'{nick_name}, enter the row (Enter a number from 1 to 3): ')
        select_cell = input(f'{nick_name}, enter the cell (Enter a number from 1 to 3): ')

        if not select_row or not select_cell:
            print('The parameters entered are empty. Try again')
            break

        select_row = int(select_row) - 1
        select_cell = int(select_cell) - 1

        if select_row > 2 or select_cell > 2 or select_row < 0 or select_cell < 0:
            print('Value is out of range. Try again')
            break

        if board[select_row][select_cell] != '':
            print('Cell is not empty. Try again')
            break

        board[select_row][select_cell] = player_symbol
        player_combinations.append((select_row, select_cell))
        
        if check_win(player_combinations): 
            total_player_wins += 1

            print(f'{Fore.GREEN}{player_now} wins!{Style.RESET_ALL} Total wins: {total_player_wins}')

            play_again = input('Play again? (Yes or No): ').lower()

            if play_again == 'yes':
                board = [['', '', ''] for _ in range(3)] 
                player_combinations.clear()
                bot_combinations.clear()
            else:
                print('Thanks for playing! :)')

                sheet = statistics.active
                sheet.title = 'Statistics'

                sheet['A1'] = 'Winner'
                sheet['B1'] = 'Loser'
                sheet['A3'] = 'Total player wins'
                sheet['B3'] = 'Total bot wins'

                sheet['A2'] = f'{nick_name}'
                sheet['B2'] = f'{bot}'
                sheet['A4'] = f'{total_player_wins}'
                sheet['B4'] = f'{total_bot_wins}'

                statistics.save("Statistics.xlsx")
                break
        else:
            player_now = bot

        if all(cell != '' for row in board for cell in row):
            print(f'{Fore.YELLOW}It\'s a draw!{Style.RESET_ALL}')
            break
        
        if player_now == bot:
            while True:
                random_row = random.randint(0, 2)
                random_cell = random.randint(0, 2)

                if board[random_row][random_cell] == '':
                    board[random_row][random_cell] = bot_symbol
                    bot_combinations.append((random_row, random_cell))
                    break
            
            if check_win(bot_combinations):
                total_bot_wins += 1
                print(f'{Fore.BLUE}{player_now} wins!{Style.RESET_ALL} Total wins: {total_bot_wins}')

                play_again = input('Play again? (Yes or No): ').lower()
                
                if play_again == 'yes':
                    board = [['', '', ''] for _ in range(3)] 
                    player_combinations.clear()
                    bot_combinations.clear()
                else:
                    print('Thanks for playing! :)')

                    sheet = statistics.active
                    sheet.title = 'Statistics'

                    sheet['A1'] = 'Winner'
                    sheet['B1'] = 'Loser'
                    sheet['A3'] = 'Total player wins'
                    sheet['B3'] = 'Total bot wins'

                    sheet['A2'] = f'{bot}'
                    sheet['B2'] = f'{nick_name}'
                    sheet['A4'] = f'{total_bot_wins}'
                    sheet['B4'] = f'{total_player_wins}'

                    statistics.save("Statistics.xlsx")

                    break

            player_now = nick_name
elif select_mode == '2':
    first_player = input('Please enter the first player\'s nickname: ')
    second_player = input('Please enter the second player\'s nickname: ')

    combinations_first_player = []
    combinations_second_player = []

    total_first_player_wins = 0
    total_second_player_wins = 0

    player_now = first_player
    symbol = 'X'

    if not first_player or not second_player:
        print('The parameters entered are empty. Try again')

    while game_is_run:
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

        select_row = input(f'{player_now}, enter the row (Enter a number from 1 to 3): ')
        select_cell = input(f'{player_now}, enter the cell (Enter a number from 1 to 3): ') 

        if not select_row or not select_cell:
            print('The parameters entered are empty. Try again')
            continue

        select_row = int(select_row) - 1
        select_cell = int(select_cell) - 1

        if select_row not in range(3) or select_cell not in range(3):
            print('Value is out of range. Try again')
            continue

        if board[select_row][select_cell] != '':
            print('Cell is not empty. Try again')
            continue

        board[select_row][select_cell] = symbol

        if player_now == first_player:
            combinations_first_player.append((select_row, select_cell))

            if check_win(combinations_first_player):
                total_first_player_wins += 1
                print(f'{Fore.GREEN}{player_now} wins!{Style.RESET_ALL} Total wins: {total_first_player_wins}')
            else:
                player_now = second_player
                symbol = 'O'
                continue
        else:
            combinations_second_player.append((select_row, select_cell))

            if check_win(combinations_second_player):
                total_second_player_wins += 1
                print(f'{Fore.GREEN}{player_now} wins!{Style.RESET_ALL} Total wins: {total_second_player_wins}')
            else:
                player_now = first_player
                symbol = 'X'
                continue

        play_again = input('Play again? (Yes or No): ').lower()
        if play_again == 'yes':
            board = [['', '', ''] for _ in range(3)] 
            combinations_first_player.clear()
            combinations_second_player.clear()
            player_now = first_player
            symbol = 'X'
        else:
            print('Thanks for playing! :)')

            sheet = statistics.active
            sheet.title = 'Statistics'

            sheet['A1'] = 'Winner'
            sheet['B1'] = 'Loser'
            sheet['A3'] = 'Total first player wins'
            sheet['B3'] = 'Total second player wins'

            sheet['A2'] = f'{first_player if total_first_player_wins > total_second_player_wins else second_player}'
            sheet['B2'] = f'{second_player if total_first_player_wins > total_second_player_wins else first_player}'
            sheet['A4'] = f'{total_first_player_wins}'
            sheet['B4'] = f'{total_second_player_wins}'

            statistics.save("Statistics.xlsx")
            break