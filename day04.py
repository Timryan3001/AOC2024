from aoc_utils import fetch_input, get_day_from_filename
import os
import time

# This file is a template for future days

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

#FETCHING INPUTS

day = get_day_from_filename(os.path.basename(__file__))


input_data = fetch_input(day)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

start_time_p1 = time.time()

def find_word_count(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    word_length = len(word)
    countp1 = 0

    # Define all eight possible directions (dx, dy)
    directions = [
        (0, 1),  # Right
        (0, -1), # Left
        (1, 0),  # Down
        (-1, 0), # Up
        (1, 1),  # Diagonal down-right
        (-1, -1),# Diagonal up-left
        (1, -1), # Diagonal down-left
        (-1, 1), # Diagonal up-right
    ]

    def is_word_at(x, y, dx, dy):
        """Check if the word exists starting from (x, y) in direction (dx, dy)."""
        for i in range(word_length):
            nx, ny = x + i * dx, y + i * dy
            if nx < 0 or nx >= rows or ny < 0 or ny >= cols:
                return False  # Out of bounds
            if grid[nx][ny] != word[i]:
                return False  # Character mismatch
        # print(f"Word '{word}' found starting at ({x}, {y}) in direction ({dx}, {dy})")
        return True

    # Traverse the grid
    for r in range(rows):
        for c in range(cols):
            for dx, dy in directions:
                if is_word_at(r, c, dx, dy):
                    # print(f"Count incremented for '{word}' at ({r}, {c}) in direction ({dx}, {dy})")
                    countp1 += 1

    return countp1

# Input grid
grid = [list(line) for line in input_data.splitlines()]

# Word to search for
word = "XMAS"

# Find and print the count
countp1 = find_word_count(grid, word)



end_time_p1 = time.time()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

start_time_p2 = time.time()

def find_x_mas(grid):
    rows = len(grid)
    cols = len(grid[0])
    countp2 = 0

    # Define the two valid patterns for the diagonals
    valid_patterns = ["MAS", "SAM"]

    # Iterate through each potential center of the X
    for r in range(1, rows - 1):  # Skip first and last rows for bounds
        for c in range(1, cols - 1):  # Skip first and last cols for bounds
            # Check the top-left to bottom-right diagonal
            diag1 = grid[r - 1][c - 1] + grid[r][c] + grid[r + 1][c + 1]
            # Check the top-right to bottom-left diagonal
            diag2 = grid[r - 1][c + 1] + grid[r][c] + grid[r + 1][c - 1]

            # Validate both diagonals
            if diag1 in valid_patterns and diag2 in valid_patterns:
                countp2 += 1

    return countp2

# Count X-MAS patterns in the grid
countp2 = find_x_mas(grid)
print(f"The X-MAS pattern appears {countp2} times in the grid.")


end_time_p2 = time.time()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# RESULTS # 
print(f"The word '{word}' appears {countp1} times in the grid.")
print(f"Execution Time for P1: {end_time_p1 - start_time_p1:.4f} seconds")
print(f"The X-Mas star appears {countp2} times in the grid.")
print(f"Execution Time for P2: {end_time_p2 - start_time_p2:.4f} seconds")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #