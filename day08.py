from aoc_utils import fetch_input, get_day_from_filename
import os
import time
import math 

# This file is a template for future days

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

#FETCHING INPUTS

day = get_day_from_filename(os.path.basename(__file__))


input_data = fetch_input(day)

grid = [list(line) for line in input_data.splitlines()]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

start_time_p1 = time.time()

import itertools
from collections import defaultdict

def parse_grid(grid):
    """Parse the grid and group antennas by frequency."""
    antennas = defaultdict(set)
    for row_idx, row in enumerate(grid):
        for col_idx, frequency in enumerate(row):
            if frequency != ".":  # Only consider antenna positions
                antennas[frequency].add(complex(row_idx, col_idx))
    bounds = complex(len(grid), len(grid[0]))  # Grid dimensions as a complex number
    return antennas, bounds

def is_in_bounds(position, bounds):
    """Check if a position is within the grid bounds."""
    return 0 <= position.real < bounds.real and 0 <= position.imag < bounds.imag

def find_antinodes(nodes, bounds, start_step=1, end_step=1):
    """Generate antinodes for a pair of antennas."""
    for node_a, node_b in itertools.combinations(nodes, 2):
        distance = node_b - node_a  # Vector between two antennas
        for node, direction in [(node_a, -1), (node_b, 1)]:  # Explore both directions
            step = start_step
            while (end_step is None or step <= end_step) and is_in_bounds(
                antinode := node + direction * step * distance, bounds
            ):
                yield antinode
                step += 1

def count_unique_antinodes(grid, include_on_antennas=False):
    """Count unique antinodes based on antenna positions."""
    antennas, bounds = parse_grid(grid)
    start_step = 0 if include_on_antennas else 1
    end_step = None if include_on_antennas else 1

    # Collect unique antinodes for all antenna frequencies
    unique_antinodes = {
        antinode
        for nodes in antennas.values()
        for antinode in find_antinodes(nodes, bounds, start_step, end_step)
    }
    return len(unique_antinodes)



# Part 1: Calculate antinodes excluding antennas
part_1_result = count_unique_antinodes(grid, include_on_antennas=False)

# Part 2: Calculate antinodes including antennas
part_2_result = count_unique_antinodes(grid, include_on_antennas=True)

end_time_p1 = time.time()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

start_time_p2 = time.time()

#part 2 goes here

end_time_p2 = time.time()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# RESULTS # 

print(part_1_result)
print(f"Execution Time for P1: {end_time_p1 - start_time_p1:.4f} seconds")
print(part_2_result)
print(f"Execution Time for P2: {end_time_p2 - start_time_p2:.4f} seconds")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #