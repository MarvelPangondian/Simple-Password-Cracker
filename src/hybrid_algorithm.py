import re
from typing import Tuple
import time
from utils import load_heuristic_password, hash_password, seconds_to_time_unit, CHARACTERS

from brute_force_algorithm import possible_combinations


def apply_transformations(word):

    transformations = set()

    # Common substitutions
    substitutions = [
        (r"a", "@"),
        (r"e", "3"),
        (r"i", "1"),
        (r"o", "0"),
        (r"s", "$"),
        (r"g", "9"),
    ]

    for pattern, replacement in substitutions:
        transformed_word = re.sub(pattern, replacement, word)
        transformations.add(transformed_word)

    return list(transformations)


def hybrid_password_cracker(hashed_target_password: str) -> Tuple[str, float, str]:
    # Load dictionary
    print("Searching using hybrid algorithm..")
    start_time = time.time()
    
    all_encountered_password = set()
    scored_passwords = load_heuristic_password()
    
    for password_not_altered, _ in scored_passwords:

        if (password_not_altered not in all_encountered_password):
            all_encountered_password.add(password_not_altered)
            hashed_password = hash_password(password_not_altered)
            
            if hashed_password == hashed_target_password:
                end_time = time.time()
                elapsed_time_seconds = end_time - start_time
                time_total, unit = seconds_to_time_unit(elapsed_time_seconds)
                return password_not_altered, time_total, unit
        else:
            continue
        
        for password in apply_transformations(password_not_altered):
            
            if (password not in all_encountered_password):
                all_encountered_password.add(password)
            else:
                continue
            
            hashed_password = hash_password(password)
            # Greedy by comparing target password with current strongest password first
            # If not a match, then try comparing the next strongest password
            if hashed_password == hashed_target_password:
                end_time = time.time()
                elapsed_time_seconds = end_time - start_time
                time_total, unit = seconds_to_time_unit(elapsed_time_seconds)
                return password, time_total, unit
            
    print("Password not found in dictionary. Falling back to brute force")
    
    for length in range(1, 6):
        for password_tuple in possible_combinations(CHARACTERS, length):
            password = ''.join(password_tuple)
            if password not in all_encountered_password:
                all_encountered_password.add(password)
            else:
                continue
            hashed_password = hash_password(password)
            if hashed_password == hashed_target_password:
                end_time = time.time()
                elapsed_time_seconds = end_time - start_time
                time_total, unit = seconds_to_time_unit(elapsed_time_seconds)
                return password,time_total, unit
            
    end_time = time.time()
    elapsed_time_seconds = end_time - start_time
    final_time, final_unit = seconds_to_time_unit(elapsed_time_seconds)
    
    return None, final_time, final_unit


