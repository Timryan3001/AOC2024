from aoc_utils import fetch_input, get_day_from_filename
import os
import time
import sys

# Fetching the input
day = get_day_from_filename(os.path.basename(__file__))
input_data = fetch_input(day)

# Processing the data into lists of integers
rows = [list(map(int, line.split())) for line in input_data.strip().split("\n")]

# satisfies the original criteria
def satisfies_criteria(row):
    differences = [row[i + 1] - row[i] for i in range(len(row) - 1)]
    abs_differences = [abs(diff) for diff in differences]
    is_increasing = all(diff > 0 for diff in differences)
    is_decreasing = all(diff < 0 for diff in differences)
    return all(diff <= 3 for diff in abs_differences) and (is_increasing or is_decreasing)

# Part 1 Logic
def part_1(rows):
    safe = 0
    for row in rows:
        if satisfies_criteria(row):
            safe += 1
    return safe

# Part 2 Logic
def part_2(rows):
    dampened_safe = 0
    for row in rows:
        if satisfies_criteria(row):
            dampened_safe += 1  # Already safe
            continue
        #removing each element in row to check if that makes it safe
        for i in range(len(row)):
            modified_row = row[:i] + row[i + 1:]
            if satisfies_criteria(modified_row):
                dampened_safe += 1
                break
    return dampened_safe


if __name__ == "__main__":
    part = input("Enter part to run (1 or 2): ").strip()
    if part == "1":
        start_time = time.time()
        result = part_1(rows)
        end_time = time.time()
        print(f"Execution Time for Part 1: {end_time - start_time:.4f} seconds")
        print("Count of lists with no jumps greater than 3 and consistent direction (Part 1):",
              result)
    elif part == "2":
        start_time = time.time()
        result = part_2(rows)
        end_time = time.time()
        print(f"Execution Time for Part 2: {end_time - start_time:.4f} seconds")
        print("Count of lists with one removal safe and consistent direction (Part 2):",
              result)
    else:
        print("Invalid input. Please enter 1 or 2.")
