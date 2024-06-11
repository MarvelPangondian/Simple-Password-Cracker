import hashlib
import time
from typing import Tuple
import string
import os
import re
import math

CHARACTERS = string.ascii_letters + string.digits + string.punctuation
PASSWORD_DICTIONARY = []
PASSWORD_GREEDY = []
PASSWORD_HEURISTIC = []
HAS_INITIALIZED = False
ATTEMPTS_PER_SECOND = 0.0

def read_all_txt_files_in_directory(directory_path, encoding='utf-8'):
    combined_lines = []
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path) and file_path.endswith('.txt'):
            with open(file_path, 'r', encoding=encoding,errors="ignore") as file:
                lines = file.readlines()
                combined_lines.extend(line.strip() for line in lines if line.strip())
                
    return combined_lines


def entropy(password: str) -> float:
    score = 0

    # Entropy calculation
    charset_size = 0
    if re.search(r"[A-Z]", password):
        charset_size += 26  # Uppercase letters
    if re.search(r"[a-z]", password):
        charset_size += 26  # Lowercase letters
    if re.search(r"\d", password):
        charset_size += 10  # Digits
    if re.search(r"[!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~]", password):
        charset_size += len("!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")  # Special characters

    if charset_size > 0:
        entropy = len(password) * math.log2(charset_size)
        score += entropy

    return round(score, 4)


def heuristic(password: str) -> float:
    score = 0
    median = 41.35
    score = entropy(password)
    return abs(score - median)


def initialize():
    # preprocessing
    global HAS_INITIALIZED
    global PASSWORD_DICTIONARY
    global PASSWORD_HEURISTIC
    global PASSWORD_GREEDY
    global ATTEMPTS_PER_SECOND
    HAS_INITIALIZED = True
    
    PASSWORD_DICTIONARY = read_all_txt_files_in_directory("src/database")
    PASSWORD_HEURISTIC = [(password, heuristic(password)) for password in PASSWORD_DICTIONARY]
    PASSWORD_GREEDY = [(password, entropy(password)) for password in PASSWORD_DICTIONARY]

    PASSWORD_HEURISTIC.sort(key=lambda x: x[1], reverse=False)
    PASSWORD_GREEDY.sort(key=lambda x: x[1], reverse=True)
    
        # Calculate possible attempts per second
    attempts = 0
    start_time = time.time()
    for length in range(1, 3 + 1):
        for password_tuple in possible_combinations(CHARACTERS, length):
            attempts += 1
            password = ''.join(password_tuple)
            hashed_password = hash_password(password)
            if hashed_password == "ABCDEFGHIJ":
                # simulate trying to break password
                continue
    end_time = time.time()
    ATTEMPTS_PER_SECOND = round(attempts / (end_time - start_time))

def load_passwords():
    global HAS_INITIALIZED
    global PASSWORD_DICTIONARY
    
    if (not HAS_INITIALIZED):
        initialize()
        
    return PASSWORD_DICTIONARY

def load_heuristic_password():
    global HAS_INITIALIZED
    global PASSWORD_HEURISTIC
    
    if (not HAS_INITIALIZED):
        initialize()
        
    return PASSWORD_HEURISTIC

def load_greedy_password():
    global HAS_INITIALIZED
    global PASSWORD_GREEDY
    
    if (not HAS_INITIALIZED):
        initialize()
        
    return PASSWORD_GREEDY


def possible_combinations(characters, repeat):
    pools = [list(characters)] * repeat
    result = [[]]
    for pool in pools:
        result = [x + [y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def seconds_to_time_unit(total_time_seconds : float) -> Tuple[float, str]:
    time_end = 0
    unit = ""
    if total_time_seconds >= 24 * 3600:
        time_end = total_time_seconds / (24 * 3600)
        unit = "days"
    elif total_time_seconds >= 3600:
        time_end = total_time_seconds / 3600
        unit = "hours"
    elif total_time_seconds >= 60:
        time_end = total_time_seconds / 60
        unit = "minutes"
    else:
        time_end = total_time_seconds
        unit = "seconds"
    return time_end,unit

def estimate_crack_time_string(password: str) -> None:
    estimate_crack_time(CHARACTERS, len(password))
    
def estimate_crack_time(character_set: str, max_length: int) -> None:
    total_attempts = 0
    character_set_size = len(character_set)
        
    # Calculate total number of attempts
    for length in range(1, max_length + 1):
        total_attempts += character_set_size ** length
    
    # Calculate time in seconds
    total_time_seconds = total_attempts / ATTEMPTS_PER_SECOND
    
    # Display time according total_time_seconds
    time_end, unit = seconds_to_time_unit(total_time_seconds)
    

    print(f"Estimated time to crack (if using brute force): {time_end:.2f} {unit}")
    

def time_addition(time1: float, unit1: str, time2: float, unit2: str) -> Tuple[float,str]:
    units = {
        "days": 86400,
        "hours": 3600,
        "minutes": 60,
        "seconds": 1
    }
    
    if unit1 not in units or unit2 not in units:
        raise ValueError("Invalid unit provided")
    
    total_seconds = time1 * units[unit1] + time2 * units[unit2]
    return seconds_to_time_unit(total_seconds)