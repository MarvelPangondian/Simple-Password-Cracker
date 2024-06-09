import hashlib
import time

def possible_combinations(characters, repeat):
    pools = [list(characters)] * repeat
    result = [[]]
    for pool in pools:
        result = [x + [y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_passwords(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]
    
def estimate_crack_time(character_set: str, max_length: int) -> None:
    total_attempts = 0
    character_set_size = len(character_set)
    
    # Calculate possible attempts per second
    attempts = 0
    start_time = time.time()
    for length in range(1, 3 + 1):
        for password_tuple in possible_combinations(character_set, length):
            attempts += 1
            password = ''.join(password_tuple)
            hashed_password = hash_password(password)
            if hashed_password == "ABCDEFGHIJ":
                # simulate trying to break password
                continue
    end_time = time.time()
    attempts_per_second = round(attempts / (end_time - start_time))
    
    # Calculate total number of attempts
    for length in range(1, max_length + 1):
        total_attempts += character_set_size ** length
    
    # Calculate time in seconds
    total_time_seconds = total_attempts / attempts_per_second
    
    # Display time according total_time_seconds
    time_end = 0
    unit = ""
    if total_time_seconds >= 24 * 3600:
        time_end = total_time_seconds / (24 * 3600)
        unit = "days"
    elif total_time_seconds >= 3600:
        time_end = total_time_seconds / 3600
        unit = "hours"
    elif total_time_seconds >= 60:
        time_end = total_time_seconds / 60
        unit = "minutes"
    else:
        time_end = total_time_seconds
        unit = "seconds"
    

    print(f"Estimated time to crack (worst case): {time_end:.2f} {unit}")
    
