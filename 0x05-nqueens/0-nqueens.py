#!/usr/bin/python3
import sys

# Input validation
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)


# Backtracking function
def solve_nqueens(N):
    solutions = []
    queens = [-1] * N  # Initialize queen positions

    def is_valid(row, col):
        for r in range(row):
            # Check for column and diagonal conflicts
            if queens[r] == col or \
               queens[r] - r == col - row or \
               queens[r] + r == col + row:
                return False
        return True

    def place_queen(row):
        if row == N:
            # Store the solution in the required format
            solution = [[r, queens[r]] for r in range(N)]
            solutions.append(solution)
            return
        for col in range(N):
            if is_valid(row, col):
                queens[row] = col  # Place queen
                place_queen(row + 1)  # Recurse for the next row
                queens[row] = -1  # Backtrack

    place_queen(0)
    return solutions


# Solve the N-Queens problem and print each solution
solutions = solve_nqueens(N)
for solution in solutions:
    print(solution)
