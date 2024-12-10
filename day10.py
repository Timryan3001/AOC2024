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

from collections import deque

def parse_grid(input_data):
    return [[int(char) for char in line.strip()] for line in input_data.splitlines()]

def find_trailheads(grid):
    trailheads = []
    for i, row in enumerate(grid):
        for j, height in enumerate(row):
            if height == 0:
                trailheads.append((i, j))
    return trailheads

def bfs_trailhead(grid, start):
    rows, cols = len(grid), len(grid[0])
    queue = deque([start])
    visited = set()
    visited.add(start)
    reachable_nines = set()
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if (nx, ny) not in visited and grid[nx][ny] == grid[x][y] + 1:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
                    if grid[nx][ny] == 9:
                        reachable_nines.add((nx, ny))
    return len(reachable_nines)

end_time_p1 = time.time()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

start_time_p2 = time.time()

def dfs_trailhead(grid, x, y, visited):
    """Part 2: Calculate the rating (distinct paths) for a trailhead."""
    rows, cols = len(grid), len(grid[0])
    if not (0 <= x < rows and 0 <= y < cols):
        return 0
    if (x, y) in visited:
        return 0
    visited.add((x, y))
    
    if grid[x][y] == 9:
        visited.remove((x, y))
        return 1
    
    distinct_paths = 0
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == grid[x][y] + 1:
            distinct_paths += dfs_trailhead(grid, nx, ny, visited)
    
    visited.remove((x, y))
    return distinct_paths

def calculate_scores_and_ratings(grid):
    trailheads = find_trailheads(grid)
    total_score = 0
    total_rating = 0
    
    for trailhead in trailheads:
        # Part 1: Calculate the score
        score = bfs_trailhead(grid, trailhead)
        total_score += score
        
        # Part 2: Calculate the rating
        rating = dfs_trailhead(grid, trailhead[0], trailhead[1], set())
        total_rating += rating
    
    return total_score, total_rating

grid = parse_grid(input_data)
score, rating = calculate_scores_and_ratings(grid)

end_time_p2 = time.time()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# RESULTS # 


print(f"Part 1: Total score of all trailheads: {score}")
print(f"Part 2: Total rating of all trailheads: {rating}")

print(f"Execution Time for P1: {end_time_p1 - start_time_p1:.4f} seconds")
print(f"Execution Time for P2: {end_time_p2 - start_time_p2:.4f} seconds")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #