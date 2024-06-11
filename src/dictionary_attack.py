from utils import hash_password, load_passwords
from typing import Tuple
from utils import seconds_to_time_unit
import time







def dictionary_attack_password_cracker(hashed_target_password: str) -> Tuple[str, float, str]:
    start_time = time.time()
    passwords = load_passwords()

    for password in passwords:
        hashed_password = hash_password(password)
        if hashed_password == hashed_target_password:
            end_time = time.time()
            elapsed_time_seconds = end_time - start_time
            time_total, unit = seconds_to_time_unit(elapsed_time_seconds)
            return password, time_total, unit

    end_time = time.time()
    elapsed_time_seconds = end_time - start_time
    time_total, unit = seconds_to_time_unit(elapsed_time_seconds)

    return None, time_total, unit
