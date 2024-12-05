from aoc_utils import fetch_input, get_day_from_filename
import os
import time
from collections import defaultdict, deque

# This file is a template for future days

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

#FETCHING INPUTS

day = get_day_from_filename(os.path.basename(__file__))


input_data = fetch_input(day)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

start_time_p1 = time.time()

def parse_input(input_data):
    sections = input_data.strip().split("\n\n")
    rules = sections[0].splitlines()
    updates = [list(map(int, update.split(','))) for update in sections[1].splitlines()]
    
    ordering_rules = []
    for rule in rules:
        x, y = map(int, rule.split('|'))
        ordering_rules.append((x, y))
    
    return ordering_rules, updates


def is_valid_update(update, rules):
    for x, y in rules:
        if x in update and y in update:
            # Both pages are present in the update, check their order
            if update.index(x) > update.index(y):
                return False
    return True


def find_middle_page(update):
    middle_index = len(update) // 2
    return update[middle_index]


def process_updates(ordering_rules, updates):
    valid_updates = []
    for update in updates:
        if is_valid_update(update, ordering_rules):
            valid_updates.append(update)
    
    middle_sum = sum(find_middle_page(update) for update in valid_updates)
    return middle_sum

# Parse the input
ordering_rules, updates = parse_input(input_data)

# Process the updates
result = process_updates(ordering_rules, updates)


end_time_p1 = time.time()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

start_time_p2 = time.time()

#rofl its cooking
def reorder_update(update, rules):
    # Build a graph from the rules
    graph = defaultdict(list)
    indegree = defaultdict(int)
    
    # Add rules to the graph
    for x, y in rules:
        if x in update and y in update:
            graph[x].append(y)
            indegree[y] += 1
            indegree.setdefault(x, 0)
    
    # Topological sort using Kahn's algorithm
    queue = deque([node for node in update if indegree[node] == 0])
    sorted_pages = []
    
    while queue:
        node = queue.popleft()
        sorted_pages.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    return sorted_pages

def process_updates_part2(ordering_rules, updates):
    invalid_updates = []
    for update in updates:
        if not is_valid_update(update, ordering_rules):
            invalid_updates.append(update)
    
    reordered_updates = [reorder_update(update, ordering_rules) for update in invalid_updates]
    middle_sum = sum(find_middle_page(update) for update in reordered_updates)
    return middle_sum

result_part2 = process_updates_part2(ordering_rules, updates)


end_time_p2 = time.time()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# RESULTS # 

print("Sum of middle pages:", result)
print(f"Execution Time for P1: {end_time_p1 - start_time_p1:.4f} seconds")
print("Sum of middle pages after reordering:", result_part2)
print(f"Execution Time for P2: {end_time_p2 - start_time_p2:.4f} seconds")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #