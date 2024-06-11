from utils import hash_password, load_greedy_password,seconds_to_time_unit
from typing import Tuple
import time

def greedy_password_cracker(hashed_target_password: str) -> Tuple[str, float, str]:

    print("Searching using greedy algorithm..")
    start_time = time.time()
    scored_passwords = load_greedy_password()

    # Sort passwords based on their heuristic score
    # Strong passwords have high score, weak passwords have low scores

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
