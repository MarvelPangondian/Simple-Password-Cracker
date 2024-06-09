from utils import hash_password,estimate_crack_time,possible_combinations
import string
import time
from typing import Tuple
from utils import CHARACTERS
from utils import seconds_to_time_unit

def brute_force_password_cracker(hashed_target_password : string) -> Tuple[str, float, str]:
    
    # All possible characters
    characters = CHARACTERS
    
    start_time = time.time()
    
    # set maximum length of password to 5, for 6 > passwords it will take days to compute
    for length in range(1, 6):
        for password_tuple in possible_combinations(characters, length):
            password = ''.join(password_tuple)
            hashed_password = hash_password(password)
            if hashed_password == hashed_target_password:
                end_time = time.time()
                elapsed_time_seconds = end_time - start_time
                time_total, unit = seconds_to_time_unit(elapsed_time_seconds)
                return password,time_total, unit
                

    end_time = time.time()
    elapsed_time_seconds = end_time - start_time
    time_total, unit = seconds_to_time_unit(elapsed_time_seconds)

    return None, time_total, unit



