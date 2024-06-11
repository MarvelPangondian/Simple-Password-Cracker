import sys
import os
import re
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

# Append the path for importing custom modules
sys.path.append("src/")
from utils import hash_password, initialize
from greedy_algorithm import greedy_password_cracker
from hybrid_algorithm import hybrid_password_cracker
from dictionary_attack import dictionary_attack_password_cracker
from heuristic_algorithm import heuristic_password_cracker
from brute_force_algorithm import brute_force_password_cracker

# Sample password lists for testing
FOUR_LETTER_PASSWORD = [
    "God5", "Act2", "1Dos", "pass", "d1ar", "Cat1", "@bcd", "1LuV", "LOVE", "3lm0",
    "1God", "word", "k@z1", "luke", "Gus3", "2Pac", "1LdL", "Joe5", "papa", "t0n1",
    "kyr3", "n3mo", "king", "Jo89", "ally"
]

LONG_PASSWORDS = [
    "subg3nius","forester","blissful", "babysexy","MUHAMMAD", "sub0m0de","janerv20","sublim3o","subflower","subbzero7",
    "tw1rl1ng","sr3dinom","jan3l3n3","substitut","subvet65","subhum@no","jdgnamjj","mewblade","subg3nius","maishajaz",
    "maisokeni", "ciscobob","cluelesss","maricela","cutie123"
]

# Function to write results to a file
def write_results_to_file(filename, time_total, time_attempts, average, password_list):
    with open(filename, 'w', encoding="utf-8", errors="ignore") as file:
        file.write(f"time total: {time_total:.2f} seconds\n")
        file.write(f"Passwords cracked: {time_attempts} out of {len(password_list)}\n")
        file.write(f"time average: {average:.2f} seconds\n")

# General test function
def test_password_cracker(cracker_function, algorithm_name, output_filename, password_list):
    print(f"{algorithm_name} test")
    time_total = 0
    time_attempts = 0
    
    for password_target in password_list:
        password_target_hash = hash_password(password_target)
        print("searching..")
        password, time = cracker_function(password_target_hash)
        
        if password:
            print(f"{algorithm_name} success: {password_target}")
            time_total += time
            time_attempts += 1
        else:
            print(f"{algorithm_name} failed: {password_target}")
    
    if time_attempts > 0:
        average = time_total / time_attempts
    else:
        average = 0

    print(f"time total: {time_total} seconds")
    print(f"Passwords cracked: {time_attempts} out of {len(password_list)}")
    print(f"time average: {average} seconds")
    
    write_results_to_file(output_filename, time_total, time_attempts, average, password_list)
    print("DONE\n")

# Initialize the system
initialize()

# Test 1
test_password_cracker(dictionary_attack_password_cracker, "Dictionary", "test/dict1.txt", FOUR_LETTER_PASSWORD)
test_password_cracker(greedy_password_cracker, "Greedy", "test/greedy1.txt", FOUR_LETTER_PASSWORD)
test_password_cracker(heuristic_password_cracker, "Heuristic", "test/heuristic1.txt", FOUR_LETTER_PASSWORD)
test_password_cracker(hybrid_password_cracker, "Hybrid", "test/hybrid1.txt", FOUR_LETTER_PASSWORD)
test_password_cracker(brute_force_password_cracker, "Brute Force", "test/brute1.txt", FOUR_LETTER_PASSWORD)


# Test 2
test_password_cracker(hybrid_password_cracker, "Hybrid", "test/hybrid2.txt", LONG_PASSWORDS)
test_password_cracker(dictionary_attack_password_cracker, "Dictionary", "test/dict2.txt", LONG_PASSWORDS)
test_password_cracker(greedy_password_cracker, "Greedy", "test/greedy2.txt", LONG_PASSWORDS)
test_password_cracker(heuristic_password_cracker, "Heuristic", "test/heuristic2.txt", LONG_PASSWORDS)
