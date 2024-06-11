from utils import hash_password, load_passwords
import re
from typing import Tuple
from utils import seconds_to_time_unit,load_heuristic_password
import time
import math

def heuristic_password_cracker(hashed_target_password: str) -> Tuple[str, float, str]:
    print("Searching using heuristic algorithm")
    start_time = time.time()
    scored_passwords = load_heuristic_password()
    # Sort passwords based on their heuristic score
    # Common passwords have scores close to 0
    scored_passwords.sort(key=lambda x: x[1], reverse=False)
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
