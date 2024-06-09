from utils import hash_password,estimate_crack_time
import string

def possible_combinations(characters, repeat):
    pools = [list(characters)] * repeat
    result = [[]]
    for pool in pools:
        result = [x + [y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)


estimate_crack_time(string.ascii_letters + string.digits + string.punctuation, 4, 1_000_000) 
