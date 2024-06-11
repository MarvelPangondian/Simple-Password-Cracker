from utils import hash_password,seconds_to_time_unit,load_heuristic_password
from typing import Tuple
import time

def heuristic_password_cracker(hashed_target_password: str) -> Tuple[str, float]:

    print("Searching using heuristic algorithm..")
    start_time = time.time()
    scored_passwords = load_heuristic_password()
    # Sort passwords based on their heuristic score
    # Common passwords have scores close to 0

    for password, _ in scored_passwords:
        hashed_password = hash_password(password)
        if hashed_password == hashed_target_password:
            end_time = time.time()
            elapsed_time_seconds = end_time - start_time
            return password, elapsed_time_seconds

    end_time = time.time()
    elapsed_time_seconds = end_time - start_time

    return None, elapsed_time_seconds
