from utils import hash_password, load_passwords
from typing import Tuple
import time

def dictionary_attack_password_cracker(hashed_target_password: str) -> Tuple[str, float]:

    print("Searching using dictionary attack..")
    start_time = time.time()
    passwords = load_passwords()

    for password in passwords:
        hashed_password = hash_password(password)
        if hashed_password == hashed_target_password:
            end_time = time.time()
            elapsed_time_seconds = end_time - start_time
            return password, elapsed_time_seconds

    end_time = time.time()
    elapsed_time_seconds = end_time - start_time

    return None, elapsed_time_seconds
