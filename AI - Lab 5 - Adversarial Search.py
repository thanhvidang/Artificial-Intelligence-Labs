import math

board = [' '] * 9
human = 'X'
computer = 'O'

def print_board(board):
    print("-------------")
    for i in range(0, 9, 3):
        print("|", board[i], "|", board[i+1], "|", board[i+2], "|")
        print("-------------")


def human_move (board):
    while True:
        try:
            move = int(input("Enter your move between 1-9: "))
            if move < 1 or move > 9:
                print("Invalid move. Please enter a number between 1-9.")
            elif board[move - 1] != ' ':
                print("That cell is already taken. Try again.")
            else:
                return move - 1
        except ValueError:
            print("Invalid move. Please enter a number between 1-9.")

def get_empty_cells(board):
    empty_cells = []
    for i in range(9):
        if board[i] == ' ':
            empty_cells.append(i)
    return empty_cells  

def check_win(board, player):
    win_positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for positions in win_positions:
        if all(board[i] == player for i in positions):
            return True
    return False

def get_best_move(board, player):
    empty_cells = get_empty_cells(board)

    # Check if the game has ended
    if check_win(board, human):
        return None, -10
    elif check_win(board, computer):
        return None, 10
    elif len(empty_cells) == 0:
        return None, 0

    # Initialize the best move and score
    best_move = None
    best_score = -math.inf if player == computer else math.inf

    # Iterate over all empty cells and evaluate the potential moves
    for cell in empty_cells:
        board[cell] = player
        score = get_best_move(board, human if player == computer else computer)[1]
        board[cell] = ' '

        # Update the best move and score based on the current move
        if player == computer:
            if score > best_score:
                best_move = cell
                best_score = score
        else:
            if score < best_score:
                best_move = cell
                best_score = score

    return best_move, best_score

def play_game():
    print_board(board)

    while True:
        # Human's turn
        human_turn = human_move (board)
        board[human_turn] = human
        print_board(board)

        if check_win(board, human):
            print("Congratulations! You won!")
            break
        elif len(get_empty_cells(board)) == 0:
            print("It's a tie!")
            break

        # Computer's turn9
        print("Computer's turn...")
        computer_move, score = get_best_move(board, computer)
        board[computer_move] = computer
        print_board(board)

        if check_win(board, computer):
            print("Sorry, you have lost the game.")
            return

play_game()