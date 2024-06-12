from utils import hash_password,possible_combinations,CHARACTERS
import string
import time
from typing import Tuple

def brute_force_password_cracker(hashed_target_password : string) -> Tuple[str, float]:
    
    print("Searching using brute force algorithm..")
    start_time = time.time()
    # set maximum length of password to 5, for 6 > passwords it will take days to compute
    for length in range(1, 6 + 1):
        for password_tuple in possible_combinations(CHARACTERS, length):
            password = ''.join(password_tuple)
            hashed_password = hash_password(password)
            if hashed_password == hashed_target_password:
                end_time = time.time()
                elapsed_time_seconds = end_time - start_time
                return password,elapsed_time_seconds
                

    end_time = time.time()
    elapsed_time_seconds = end_time - start_time
    return None, elapsed_time_seconds



