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

def parse_disk_map(input_data):
    """Parse the input string to separate file and free space lengths."""
    files = []
    free_space = []
    is_file = True
    for char in input_data:
        if is_file:
            files.append(int(char))
        else:
            free_space.append(int(char))
        is_file = not is_file
    return files, free_space

def compact_disk_individual_blocks(files, free_space):
    """Simulate the compaction of the disk by moving individual blocks."""
    disk = []
    file_id = 0
    for file_size, space_size in zip(files, free_space):
        disk.extend([file_id] * file_size)
        disk.extend([-1] * space_size)
        file_id += 1
    if len(files) > len(free_space):
        disk.extend([file_id] * files[-1])
    
    leftmost_free = 0
    while leftmost_free < len(disk):
        if disk[leftmost_free] == -1:
            for rightmost_file in range(len(disk) - 1, leftmost_free, -1):
                if disk[rightmost_file] != -1:
                    disk[leftmost_free], disk[rightmost_file] = disk[rightmost_file], -1
                    break
        leftmost_free += 1
    return disk

def compact_disk_whole_files(files, free_space):
    """Simulate the compaction of the disk by moving whole files."""
    disk = []
    file_id = 0
    for file_size, space_size in zip(files, free_space):
        disk.extend([file_id] * file_size)
        disk.extend([-1] * space_size)
        file_id += 1
    if len(files) > len(free_space):
        disk.extend([file_id] * files[-1])
    
    # Move files in decreasing order of file ID
    for file_id in range(len(files) - 1, -1, -1):
        file_start = disk.index(file_id)
        file_size = files[file_id]
        # Check all spans of free space to the left
        for i in range(file_start):
            if all(disk[j] == -1 for j in range(i, i + file_size)):
                # Move the file
                disk = (
                    disk[:i]
                    + [file_id] * file_size
                    + disk[i + file_size:file_start]
                    + [-1] * file_size
                    + disk[file_start + file_size:]
                )
                break
    return disk

def calculate_checksum(disk):
    """Calculate the checksum of the disk."""
    checksum = 0
    for position, block in enumerate(disk):
        if block != -1:
            checksum += position * block
    return checksum


# Parse the input
files, free_space = parse_disk_map(input_data)

# Part 1: Compact by individual blocks
compacted_disk_blocks = compact_disk_individual_blocks(files, free_space)
checksum_part1 = calculate_checksum(compacted_disk_blocks)

# Part 2: Compact by whole files
compacted_disk_files = compact_disk_whole_files(files, free_space)
checksum_part2 = calculate_checksum(compacted_disk_files)

# Output results
print("Filesystem checksum (Part 1):", checksum_part1)
print("Filesystem checksum (Part 2):", checksum_part2)



end_time_p1 = time.time()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# RESULTS # 

print(f"Execution Time for P1: {end_time_p1 - start_time_p1:.4f} seconds")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #