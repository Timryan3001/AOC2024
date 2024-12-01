from aoc_utils import fetch_input, get_day_from_filename
import os
from collections import Counter
import time

# Dynamically get the day number from the filename
day = get_day_from_filename(os.path.basename(__file__))  # Pass the script's own filename

# Fetch the input for the current day
input_data = fetch_input(day)

# Start timing
start_time_p1 = time.time()

# PART 1

# Parse the input into two lists
lines = input_data.strip().split("\n")
column1 = []
column2 = []

for line in lines:
    col1, col2 = map(int, line.split())  # Split each line into two numbers
    column1.append(col1)
    column2.append(col2)

# Sort the lists
column1.sort()
column2.sort()

# Perform element-wise subtraction
result = [abs(col2 - col1) for col1, col2 in zip(column1, column2)]

part1_sol = sum(result)

# print("Column 1:", column1)
# print("Column 2:", column2)
# print("Result (Column2 - Column1):", result)
print("Part 1:", part1_sol)

end_time_p1 = time.time()


# PART 2

start_time_p2 = time.time()

# Count occurrences of each number in column2
column2_counts = Counter(column2)

# Find occurrences of numbers in column1 within column2
occurrences = {num: column2_counts[num] for num in column1}

# Step 3: Multiply each number in column1 by its occurrences in column2
multiplications = [col1 * column2_counts[col1] for col1 in column1]

# Step 4: Sum up the results
part2_sol = sum(multiplications)

end_time_p2 = time.time()

print("Part 2:", part2_sol)

print(f"Execution Time for P1: {end_time_p1 - start_time_p1:.4f} seconds")
print(f"Execution Time for P2: {end_time_p2 - start_time_p2:.4f} seconds")