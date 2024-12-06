function solveNQueens(board, row):
    if row == N:
        return true
    for col from 0 to N-1:
        if isSafe(row, col):
            board[row][col] = 1
            if solveNQueens(board, row + 1) is true:
                return true
            board[row][col] = 0
    return false

function isSafe(row, col):
    // Check if no queen is in the same column
    // Check if no queen is in the same diagonal (both left and right)
    // Check if no queen is in the same row (optional)

function printSolution(board):
    // Print the chessboard configuration with queens placed
