from aoc_utils import fetch_input, get_day_from_filename
import os
import time
import re

# This file is a template for future days

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

#FETCHING INPUTS

day = get_day_from_filename(os.path.basename(__file__))


input_data = fetch_input(day)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

start_time_p1 = time.time()

# Regex to match the pattern mul(num1,num2)
mul_pattern = r"mul\((\d+),(\d+)\)"

# Find all matches
matches = re.findall(mul_pattern, input_data)

# Calculate the sum of the products
total_sum = sum(int(a) * int(b) for a, b in matches)

end_time_p1 = time.time()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

start_time_p2 = time.time()

#part 2 goes here
do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"

# Initialize variables
enabled = True
conditional_total_sum = 0

# Process the input
for match in re.finditer(f"{do_pattern}|{dont_pattern}|{mul_pattern}", input_data):
    match_str = match.group(0)

    if match_str == "do()":
        enabled = True
    elif match_str == "don't()":
        enabled = False
    else:
        # Match mul(num1, num2)
        mul_match = re.match(mul_pattern, match_str)
        if mul_match and enabled:
            a, b = map(int, mul_match.groups())
            conditional_total_sum += a * b

end_time_p2 = time.time()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# RESULTS # 

print("Total Sum:", total_sum)
print(f"Execution Time for P1: {end_time_p1 - start_time_p1:.4f} seconds")

print("Conditional total Sum:", conditional_total_sum)
print(f"Execution Time for P2: {end_time_p2 - start_time_p2:.4f} seconds")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #