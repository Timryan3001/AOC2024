import requests
import os
from dotenv import load_dotenv
import re


load_dotenv()

SESSION_COOKIE = os.getenv("SESSION")
BASE_URL = "https://adventofcode.com/2024/day/{day}/input"

def fetch_input(day, save_to_file=True):
    """
    Fetch the input for the specified AoC day.
    Args:
        day (int): The day of the challenge.
        save_to_file (bool): Whether to save the input to a file.
    Returns:
        str: The input as a string.
    """
    url = BASE_URL.format(day=day)
    cookies = {"session": SESSION_COOKIE}
    response = requests.get(url, cookies=cookies)
    if response.status_code == 200:
        input_data = response.text.strip()  # Remove any trailing whitespace
        if save_to_file:
            os.makedirs("inputs", exist_ok=True)
            with open(f"inputs/day{day}.txt", "w") as f:
                f.write(input_data)
        return input_data
    else:
        raise Exception(f"Failed to fetch input for day {day}. Status code: {response.status_code}")
    

def get_day_from_filename(filename=None):
    """
    Extracts the day number from the filename provided.
    Args:
        filename (str): The filename to extract the day from. If None, defaults to __file__.
    Returns:
        int: The day number.
    """
    # If no filename is passed, use __file__ (current file)
    if filename is None:
        filename = os.path.basename(__file__)
    
    print(f"Filename: {filename}")  # Debugging line
    match = re.search(r'day(\d+)', filename, re.IGNORECASE)
    if not match:
        raise ValueError("Could not find 'dayXX' in the filename. Ensure the script is named like 'day01.py'.")
    
    day = match.group(1)
    return int(day.lstrip('0'))
