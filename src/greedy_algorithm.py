from utils import hash_password, load_greedy_password
from typing import Tuple
import time

def greedy_password_cracker(hashed_target_password: str) -> Tuple[str, float]:

    print("Searching using greedy algorithm..")
    start_time = time.time()
    
    scored_passwords = load_greedy_password()
    
    for password, _ in scored_passwords:
        hashed_password = hash_password(password)

        # Greedy by comparing target password with current strongest password first
        # If not a match, then try comparing the next strongest password
        if hashed_password == hashed_target_password:
            end_time = time.time()
            elapsed_time_seconds = end_time - start_time

            return password, elapsed_time_seconds

    end_time = time.time()
    elapsed_time_seconds = end_time - start_time

    return None, elapsed_time_seconds
