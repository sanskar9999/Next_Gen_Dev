import random

def print_board(board):
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

def empty_cells(board):
    return [i for i, x in enumerate(board) if x == " "]

def is_winner(board, player):
    win_states = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]
    return any(all(board[i] == player for i in state) for state in win_states)

def game_over(board):
    return is_winner(board, "X") or is_winner(board, "O") or len(empty_cells(board)) == 0

def minimax(board, depth, is_maximizing):
    if is_winner(board, "O"):
        return 1
    if is_winner(board, "X"):
        return -1
    if len(empty_cells(board)) == 0:
        return 0
    
    if is_maximizing:
        best_score = float('-inf')
        for move in empty_cells(board):
            board[move] = "O"
            score = minimax(board, depth + 1, False)
            board[move] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for move in empty_cells(board):
            board[move] = "X"
            score = minimax(board, depth + 1, True)
            board[move] = " "
            best_score = min(score, best_score)
        return best_score

def get_best_move(board):
    best_score = float('-inf')
    best_move = None
    for move in empty_cells(board):
        board[move] = "O"
        score = minimax(board, 0, False)
        board[move] = " "
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def play_game():
    board = [" " for _ in range(9)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    
    while not game_over(board):
        # Human's turn
        while True:
            try:
                move = int(input("Enter your move (1-9): ")) - 1
                if move in empty_cells(board):
                    board[move] = "X"
                    break
                else:
                    print("That cell is already occupied. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")
        
        print_board(board)
        
        if game_over(board):
            break
        
        # AI's turn
        print("AI is making a move...")
        ai_move = get_best_move(board)
        board[ai_move] = "O"
        print_board(board)
    
    if is_winner(board, "X"):
        print("Congratulations! You win!")
    elif is_winner(board, "O"):
        print("AI wins! Better luck next time.")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    play_game()
