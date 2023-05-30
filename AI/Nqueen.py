def is_safe(board, row, col, N):
    # Check if the current position is safe for a queen

    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # The position is safe
    return True


def solve_n_queens_util(board, col, N, solutions):
    # Base case: If all queens are placed, add the solution
    if col == N:
        solution = []
        for i in range(N):
            row_string = ""
            for j in range(N):
                if board[i][j] == 1:
                    row_string += "Q "
                else:
                    row_string += "- "
            solution.append(row_string.strip())
        solutions.append(solution)
        return

    # Try placing a queen in each row of the current column
    for i in range(N):
        if is_safe(board, i, col, N):
            # Place the queen
            board[i][col] = 1

            # Recur for the next column
            solve_n_queens_util(board, col + 1, N, solutions)

            # Backtrack: Remove the queen from the current position
            board[i][col] = 0


def solve_n_queens(N):
    board = [[0] * N for _ in range(N)]  # Initialize the chessboard
    solutions = []  # Store the solutions

    # Solve the N-Queens problem
    solve_n_queens_util(board, 0, N, solutions)

    return solutions


# Test the function
N = 4
solutions = solve_n_queens(N)

# Print the solutions
for i, solution in enumerate(solutions):
    print(f"Solution {i+1}:")
    for row in solution:
        print(row)
    print()
