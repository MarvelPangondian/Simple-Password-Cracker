from utils import hash_password, load_passwords
import re
from typing import Tuple
from utils import seconds_to_time_unit
import time
import math


# TODO : make and test greedy based password cracker algorithm


def heuristic(password: str) -> float:
    score = 0

    # Entropy calculation
    charset_size = 0
    if re.search(r"[A-Z]", password):
        charset_size += 26  # Uppercase letters
    if re.search(r"[a-z]", password):
        charset_size += 26  # Lowercase letters
    if re.search(r"\d", password):
        charset_size += 10  # Digits
    if re.search(r"[!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~]", password):
        charset_size += len("!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")  # Special characters

    if charset_size > 0:
        entropy = len(password) * math.log2(charset_size)
        score += entropy

    return round(score, 4)


def greedy_password_cracker(hashed_target_password: str) -> Tuple[str, float, str]:
    start_time = time.time()
    passwords = load_passwords()

    scored_passwords = [(password, heuristic(password)) for password in passwords]

    # Sort passwords based on their heuristic score
    # Strong passwords have high score, weak passwords have low scores
    scored_passwords.sort(key=lambda x: x[1], reverse=True)

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
