from sympy import *
from art import *
from utils import hash_password, estimate_crack_time_string, initialize,seconds_to_time_unit
from brute_force_algorithm import brute_force_password_cracker
from greedy_algorithm import greedy_password_cracker
from dictionary_attack import dictionary_attack_password_cracker
from heuristic_algorithm import heuristic_password_cracker
from hybrid_algorithm import hybrid_password_cracker

def find_password(choice: int):
    cracked_password = None
    time_cracked = 0.0
    unit_time = ""
    password = input("Enter password: ")
    print()
    hash_password_target = hash_password(password)
    estimate_crack_time_string(password)
    
    if choice == 1:
        cracked_password, time_cracked = dictionary_attack_password_cracker(hash_password_target)
    elif choice == 2:
        cracked_password, time_cracked = brute_force_password_cracker(hash_password_target)
    elif choice == 3:
        cracked_password, time_cracked = greedy_password_cracker(hash_password_target)
    elif choice == 4:
        cracked_password, time_cracked  = heuristic_password_cracker(hash_password_target)
    elif choice == 5:
        cracked_password, time_cracked = hybrid_password_cracker(hash_password_target)
    
    time_cracked, unit_time = seconds_to_time_unit(time_cracked)
    
    return cracked_password, time_cracked, unit_time

def main_menu():
    initialize()
    tprint("Password Cracker")
    user_input = 0

    while user_input != 6:
        print(" main menu ".center(50, "="))
        print("Pick method to use!")
        print("1. Pure Dictionary Attack")
        print("2. Brute Force")
        print("3. Greedy")
        print("4. Heuristic")
        print("5. Hybrid")
        print("6. End program")

        try:
            user_input = int(input("Choice: "))
            if 1 <= user_input <= 5:
                cracked_password, time_cracked, unit_time = find_password(user_input)
                if cracked_password:
                    print("Cracked password: " + cracked_password)
                    print(f"Time taken: {time_cracked:.2f} {unit_time}")
                    print()
                else:
                    print("Unable to crack password...")
            elif user_input != 6:
                print("Please enter a valid choice between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main_menu()
    tprint("Thank You !")