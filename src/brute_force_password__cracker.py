from utils import hash_password,estimate_crack_time,possible_combinations
import string
import time
from typing import Generator, Iterable, List, Optional, Tuple, Union

def brute_force_password_cracker(hashed_target_password : string) -> Tuple[str, float]:
    
    # All possible characters
    characters = string.ascii_letters + string.digits + string.punctuation
    
    start_time = time.time()
    
    # set maximum length of password to 5, for 6 > passwords it will take days to compute
    for length in range(1, 6):
        for password_tuple in possible_combinations(characters, length):
            password = ''.join(password_tuple)
            hashed_password = hash_password(password)
            if hashed_password == hashed_target_password:
                print(f"Password cracked: {password}")
                end_time = time.time()
                elapsed_time_seconds = end_time - start_time
                return password,elapsed_time_seconds
                

    end_time = time.time()
    elapsed_time_seconds = end_time - start_time

    
    return None, elapsed_time_seconds


# brute_force_password_cracker("asdasdgfsdfasdasd")
password, time_taken = brute_force_password_cracker(hash_password("abc"))
print("Password : " + str(password))
print("Time taken : " + str(time_taken ) + " seconds")
