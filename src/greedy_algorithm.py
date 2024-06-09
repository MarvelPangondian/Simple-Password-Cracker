from utils import hash_password, load_passwords
import re
from typing import Tuple
from utils import seconds_to_time_unit
import time



# TODO : make and test greedy based password cracker algorithm

def heuristic(password: str) -> int:
    
    min_length = 8
    score = 0

    # Check if password length is within the allowed range
    if min_length <= len(password):
        score += 1
    
    # Check for different character types and add to the score
    # if password contains uppercase, lowercase, digit, and special characters
    for pattern, weight in [(r"[A-Z]", 2), (r"[a-z]", 2), (r"\d", 2), (r"[!@#$%^&*()-_+=]", 3)]:
        if re.search(pattern, password):
            score += weight
    
    # Add points based on the number of unique characters in the password
    unique_chars = len(set(password))
    if unique_chars >= 10:
        score += 2
    elif unique_chars >= 5:
        score += 1
    
    return score

def greedy_password_cracker(hashed_target_password: str, dictionary_file: str) -> Tuple[str, float, str]:
    start_time = time.time()
    passwords = load_passwords(dictionary_file)
    scored_passwords = [(password, heuristic(password)) for password in passwords]
    # Sort passwords based on their heuristic score
    # Strong passwords have high score, weak passwords have low scores
    scored_passwords.sort(key=lambda x: x[1], reverse=True)
    
    for password, _ in scored_passwords:
        hashed_password = hash_password(password)
        
        # Greedy by comparing target password with current strongest password first
        # If not a match, then try comparing the next strongest password
        if hashed_password == hashed_target_password:
            end_time = time.time()
            elapsed_time_seconds = end_time - start_time
            time_total, unit = seconds_to_time_unit(elapsed_time_seconds)
            return password, time_total, unit

    end_time = time.time()
    elapsed_time_seconds = end_time - start_time
    time_total, unit = seconds_to_time_unit(elapsed_time_seconds)
    
    return None, time_total, unit