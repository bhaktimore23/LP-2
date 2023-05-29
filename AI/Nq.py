def is_safe(board, row, col):
    for i in range(col):
        if board[i] in (row, row - (col - i), row + (col - i)):
            return False
    return True

def solve_n_queens_util(board, col, n, solutions, current_solution):
    if col == n:
        solutions.append(list(current_solution))
        return
    
    for row in range(n):
        if is_safe(board, row, col):
            board[col] = row
            current_solution.append(''.join(('Q' if i == row else '-') for i in range(n)))
            solve_n_queens_util(board, col + 1, n, solutions, current_solution)
            current_solution.pop()
            
def solve_n_queens(n):
    board = [0] * n
    solutions = []
    solve_n_queens_util(board, 0, n, solutions, [])
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
