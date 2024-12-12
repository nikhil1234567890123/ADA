from tabulate import tabulate

def print_solution(board):
    n = len(board)
    formatted_board = [[' ' for _ in range(n)] for _ in range(n)]
    for row, col in enumerate(board):
        formatted_board[row][col] = 'Q'
    print(tabulate(formatted_board, tablefmt="grid"))

def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_n_queens(board, row, n):
    if row == n:
        print_solution(board)
        return
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_n_queens(board, row + 1, n)

def n_queens(n):
    board = [-1] * n
    solve_n_queens(board, 0, n)

if __name__ == "__main__":
    num_queens = int(input("Enter the number of Queens: "))
    n_queens(num_queens)
