import sys
sys.path.append("src/")

from utils import hash_password
from brute_force_algorithm import brute_force_password_cracker
from greedy_algorithm import greedy_password_cracker
from hybrid_algorithm import hybrid_password_cracker
from utils import estimate_crack_time_string

def test_greedy():

    password_target = "pass"
    password_target_hash = hash_password(password_target)
    estimate_crack_time_string(password_target)
    
    print("searching..")
    password, time, unit = greedy_password_cracker(password_target_hash,"src/database/dictionary.txt")
    if (password != None):
        print(f"Password : {password}")
        print(f"Time taken : {time:.2f} {unit}")

def test_hybrid():
    password_target = "anji"
    
    
    password_target_hash = hash_password(password_target)
    estimate_crack_time_string(password_target)
    
    print("searching..")
    password, time, unit = hybrid_password_cracker(password_target_hash,"src/database/dictionary.txt")
    if (password != None):
        print(f"Password : {password}")
        print(f"Time taken : {time:.2f} {unit}")

    
    
test_hybrid()