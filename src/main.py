from utils import hash_password
from brute_force_algorithm import brute_force_password_cracker
from utils import estimate_crack_time_string
def main():
    password_target = "pa"
    password_target_hash = hash_password(password_target)
    estimate_crack_time_string(password_target)
    
    password, time, unit = brute_force_password_cracker(password_target_hash)
    
    if (password != None):
        print(f"Password : {password}")
        print(f"Time taken : {time} {unit}")

if __name__ == "__main__":
    main()