from constants import *
from errors import *

def get_player_choice(board, player):
    def check_number_fits_size(player_column):
        if not 0 <= player_column <= COLS:
            raise OutOfRangeError(f"Select a number between 1 and {COLS}")           

    def check_choice_coordinates(row, col):
        if (row, col) == (None, None):
            raise FullColError("This column is full, select another one.")
    while True:
        try:
            player_column = int(input(f"Player {player}, please choose a column\n"))
            check_number_fits_size(player_column)
            row, col = get_choice_coordinates(board, player_column, player)
            check_choice_coordinates(row, col)
        except ValueError as e:
            print("Please be kind to provide a digit :)")
            continue
        except OutOfRangeError as e:
            print(e)
            continue
        except FullColError as e:
            print(e)
            continue
        return row, col

def get_choice_coordinates(board, choice, player):
    col = choice - 1
    for row in range(len(board) - 1, -1, -1):
        if board[row][col] == 0:
            board[row][col] = player
            return row, col
    return None, None

def check_for_winner(matrix, row_index, col_index, player):
    for row_direction, col_direction in DIRECTIONS:
        connect_count = 1

        for i in range(1, 4):
            row = row_index + row_direction * i
            col = col_index + col_direction * i
            if 0 <= row < ROWS and 0 <= col < COLS and matrix[row][col] == player:
                connect_count += 1
            else:
                break
            
        for i in range(1, 4):
            row = row_index - row_direction * i
            col = col_index - col_direction * i
            if 0 <= row < ROWS and 0 <= col < COLS and matrix[row][col] == player:
                connect_count += 1
            else:
                break

        if connect_count >= 4:
            return True

    return False 



def play_game():
    board = [[0 for x in range(COLS)] for _ in range(ROWS)]
    turn = 1
    while True:
        player_number = 1 if turn % 2 != 0 else 2

        player_row, player_col = get_player_choice(board, player_number)    

        [print(row) for row in board]

        if check_for_winner(board, player_row, player_col, player_number):
            print(f"Player {player_number} is Winner!")
            break

        turn += 1 
        
play_game()