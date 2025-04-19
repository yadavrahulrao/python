def print_board(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print("\n")
def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col]:
            return False
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j]:
            return False
        i -= 1
        j += 1
    return True
def solve_n_queens_util(board, row, n, solutions):
    if row == n:
        solution = ["".join("Q" if col else "." for col in row) for row in board]
        solutions.append(solution)
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens_util(board, row + 1, n, solutions)
            board[row][col] = 0  
def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_n_queens_util(board, 0, n, solutions)
    return solutions
n = 8  
solutions = solve_n_queens(n)
print(f"Total solutions for {n}-Queens: {len(solutions)}\n")
for idx, sol in enumerate(solutions, 1):
    print(f"Solution:")
    for row in sol:
        print(row)
    print()
