import hashlib
import string
from typing import Tuple

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_passwords(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]
    
def estimate_crack_time(character_set: str, max_length: int, attempts_per_second: int) -> None:
    total_attempts = 0
    character_set_size = len(character_set)
    
    # Calculate total number of attempt
    for length in range(1, max_length + 1):
        total_attempts += character_set_size ** length
    
    # Calculate time in seconds
    total_time_seconds = total_attempts / attempts_per_second
    
    # Display time according total_time_seconds
    time = 0
    unit = ""
    if total_time_seconds >= 24 * 3600:
        time = total_time_seconds / (24 * 3600)
        unit = "days"
    elif total_time_seconds >= 3600:
        time = total_time_seconds / 3600
        unit = "hours"
    elif total_time_seconds >= 60:
        time = total_time_seconds / 60
        unit = "minutes"
    else:
        time = total_time_seconds
        unit = "seconds"

    
    print(f"Estimated time to crack (worst case): {time:.2f} {unit}")
    
