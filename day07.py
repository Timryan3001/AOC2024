from aoc_utils import fetch_input, get_day_from_filename
import os
import time
from itertools import product

# This file is a template for future days

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

#FETCHING INPUTS

day = get_day_from_filename(os.path.basename(__file__))

input_data = fetch_input(day)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

start_time_p1 = time.time()

from itertools import product

# Parse the input data
lines = input_data.strip().split('\n')
valid_numbers = []

# for line in lines:
#     left, right = line.split(':')
#     target = int(left.strip())
#     numbers = list(map(int, right.strip().split()))
    
#     # Generate all combinations of + and *
#     n = len(numbers) - 1  # Number of operators needed
#     for operators in product('+*', repeat=n):
#         # Build the expression
#         expression = str(numbers[0])
#         for num, op in zip(numbers[1:], operators):
#             expression += f" {op} {num}"
        
#         # Evaluate the expression left-to-right
#         tokens = expression.split()
#         result = int(tokens[0])
#         for i in range(1, len(tokens), 2):
#             op = tokens[i]
#             num = int(tokens[i + 1])
#             if op == '+':
#                 result += num
#             elif op == '*':
#                 result *= num
        
#         # Check if the result matches the target
#         if result == target:
#             valid_numbers.append(target)
#             break

# # Compute the sum of valid numbers
# result_sum = sum(valid_numbers)



end_time_p1 = time.time()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

start_time_p2 = time.time()

def evaluate_expression(numbers, target, idx=0, current_value=0):
    """
    Recursive function to evaluate possible results with +, *, and || operators.
    """
    if idx == len(numbers):  # Base case: all numbers processed
        return current_value == target

    # Try all operators at this position
    num = numbers[idx]
    if idx == 0:
        # First number: initialize with its value
        return evaluate_expression(numbers, target, idx + 1, num)

    # Try addition
    if evaluate_expression(numbers, target, idx + 1, current_value + num):
        return True

    # Try multiplication
    if evaluate_expression(numbers, target, idx + 1, current_value * num):
        return True

    # Try concatenation (convert numbers to strings)
    concatenated_value = int(str(current_value) + str(num))
    if evaluate_expression(numbers, target, idx + 1, concatenated_value):
        return True

    return False


def sum_valid_equations(input_data):
    """
    Parse input data and sum the test values that can be validated.
    """
    lines = input_data.strip().split('\n')
    valid_numbers = []

    for line in lines:
        left, right = line.split(':')
        target = int(left.strip())
        numbers = list(map(int, right.strip().split()))

        if evaluate_expression(numbers, target):
            valid_numbers.append(target)

    return sum(valid_numbers)

result = sum_valid_equations(input_data)

end_time_p2 = time.time()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# RESULTS # 
# print(f"Sum of valid numbers: {result_sum}")
print(f"Execution Time for P1: {end_time_p1 - start_time_p1:.4f} seconds")
print(f"Sum of valid numbers: {result}")
print(f"Execution Time for P2: {end_time_p2 - start_time_p2:.4f} seconds")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #