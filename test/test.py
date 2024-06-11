import sys
sys.path.append("src/")

from utils import hash_password
from brute_force_algorithm import brute_force_password_cracker
from greedy_algorithm import greedy_password_cracker
from hybrid_algorithm import hybrid_password_cracker
from dictionary_attack import dictionary_attack_password_cracker
from utils import estimate_crack_time_string, initialize

import re
import math

def test_greedy():

    password_target = "password"
    password_target_hash = hash_password(password_target)
    estimate_crack_time_string(password_target)
    
    print("searching..")
    password, time, unit = greedy_password_cracker(password_target_hash)
    if (password != None):
        print(f"Password : {password}")
        print(f"Time taken : {time:.2f} {unit}")

def test_hybrid():
    password_target = "password"
    
    
    password_target_hash = hash_password(password_target)
    estimate_crack_time_string(password_target)
    
    print("searching..")
    password, time, unit = hybrid_password_cracker(password_target_hash)
    if (password != None):
        print(f"Password : {password}")
        print(f"Time taken : {time:.2f} {unit}")

    
    
def test_dictionary():
    password_target = "password"
    
    
    password_target_hash = hash_password(password_target)
    estimate_crack_time_string(password_target)
    
    print("searching..")
    password, time, unit = dictionary_attack_password_cracker(password_target_hash)
    if (password != None):
        print(f"Password : {password}")
        print(f"Time taken : {time:.2f} {unit}")


# initialize()
# test_greedy()




# Example usage
# print(apply_transformations("password"))
# initialize()
# test_hybrid()


initialize()
test_dictionary()



