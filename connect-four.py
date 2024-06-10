ROWS = 6
COLS = 7

directions = [
    (0, 1),  # Horizontal
    (1, 0),  # Vertical
    (1, 1),  # Diagonal \
    (1, -1)  # Diagonal /
]


class FullColError(Exception):
    pass


def get_player_choice(player):
    while True:
        try:
            player_colum = int(input(f"Player {player}, please choose a column\n"))
            if not 0 <= player_colum <= COLS:
                print(f"Select a number between 1 and {COLS}")
                continue
        except ValueError:
            print("Enter a valid digit")
            continue
        return player_colum


def add_player_choice(matrix, choice, player):
    col = choice - 1
    for row in range(len(board) - 1, -1, -1):
        if matrix[row][col] == 0:
            matrix[row][col] = player
            return row, col
    raise FullColError


def check_for_winner(matrix, row_index, col_index, player):
    for row_direction, col_direction in directions:
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

board = [[0 for x in range(COLS)] for _ in range(ROWS)]

turn = 1
while True:
    player_number = 1 if turn % 2 != 0 else 2

    player_choice = get_player_choice(player_number)

    try:
        player_row, player_col = add_player_choice(board, player_choice, player_number)
    except FullColError:
        print("This column is full, select another one.")
        continue

    [print(row) for row in board]

    if check_for_winner(board, player_row, player_col, player_number):
        print(f"Player {player_number} is Winner!")
        break

    turn += 1 