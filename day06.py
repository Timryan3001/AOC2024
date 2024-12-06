from aoc_utils import fetch_input, get_day_from_filename
import os
import time
import matplotlib.pyplot as plt

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

#FETCHING INPUTS

day = get_day_from_filename(os.path.basename(__file__))

input_data = fetch_input(day)

#create the 2d array
grid = [list(line) for line in input_data.splitlines()]
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

start_time_p1 = time.time()


# Define directions and locate starting position
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # NORTH, EAST, SOUTH, WEST
direction_index = 0  # Initially facing NORTH
start_x, start_y = None, None

# Find the starting position (^)
for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell == "^":
            start_x, start_y = x, y
            grid[y][x] = "."  # Replace with empty space
            break
    if start_x is not None:
        break

# Initialize variables
x, y = start_x, start_y
visited_positions = set()  # Use a set to track distinct positions
visited_positions.add((x, y))

# Simulate guard's movement
while True:
    # Calculate the next position
    next_x = x + directions[direction_index][0]
    next_y = y + directions[direction_index][1]
    
    # Check if the next position is out of bounds
    if next_x < 0 or next_y < 0 or next_y >= len(grid) or next_x >= len(grid[0]):
        break  # Guard exits the mapped area

    # If there's an obstacle ahead, turn right
    if grid[next_y][next_x] == "#":
        direction_index = (direction_index + 1) % 4
    else:
        # Move forward
        x, y = next_x, next_y
        visited_positions.add((x, y))

end_time_p1 = time.time()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

start_time_p2 = time.time()

def find_loop_positions(grid, start_x, start_y, visited_positions):
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # NORTH, EAST, SOUTH, WEST

    def simulate_with_obstruction(grid, obstruction):
        visited = set()
        x, y = start_x, start_y
        direction_index = 0

        # Add the obstruction temporarily
        if obstruction:
            ox, oy = obstruction
            grid[oy][ox] = "#"

        while True:
            if (x, y, direction_index) in visited:
                # Loop detected
                break
            visited.add((x, y, direction_index))

            # Calculate the next position
            next_x = x + directions[direction_index][0]
            next_y = y + directions[direction_index][1]

            # Check bounds
            if next_x < 0 or next_y < 0 or next_y >= len(grid) or next_x >= len(grid[0]):
                visited.clear()  # Guard exits the grid
                break

            # Check for obstacle
            if grid[next_y][next_x] == "#":
                # Turn right
                direction_index = (direction_index + 1) % 4
            else:
                # Move forward
                x, y = next_x, next_y

        # Remove the obstruction
        if obstruction:
            ox, oy = obstruction
            grid[oy][ox] = "."

        return visited

    # Natural loop detection (without obstructions)
    natural_loop = simulate_with_obstruction(grid, None)

    # Try adding an obstruction only at visited positions
    valid_positions = set()
    for x, y in visited_positions:
        if grid[y][x] == "." and (x, y) != (start_x, start_y):  # Skip non-empty cells and start position
            loop_with_obstruction = simulate_with_obstruction(grid, (x, y))
            if loop_with_obstruction and loop_with_obstruction != natural_loop:
                valid_positions.add((x, y))

    return valid_positions


# Parse the input into a grid
grid = [list(line) for line in input_data.splitlines()]

# Find the starting position (^)
start_x, start_y = None, None
for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell == "^":
            start_x, start_y = x, y
            grid[y][x] = "."  # Replace with empty space
            break
    if start_x is not None:
        break

# Use the visited positions from the first part
visited_positions = {(x, y) for x, y in visited_positions}  # Assume you already have this from Part 1

# Find valid positions for obstruction
valid_positions = find_loop_positions(grid, start_x, start_y, visited_positions)

# Output results
print("Number of valid obstruction positions:", len(valid_positions))


end_time_p2 = time.time()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# RESULTS # 

# Output results
print("Guard exited at:", (x, y))
print("Positions visited:", len(visited_positions))
print(f"Execution Time for P1: {end_time_p1 - start_time_p1:.4f} seconds")

print("Number of valid obstruction positions:", len(valid_positions))
print(f"Execution Time for P2: {end_time_p2 - start_time_p2:.4f} seconds")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #