from typing import List, Tuple
import random
import string

SIZES = range(1, 50)

UPPER = 50
LOWER = -50

# These functions generate inputs for tested functions
# It is neccessary to provide this kind of generator for testing your funtion
# Generators always have to yield size and sample input as tuple

def generate_integers() -> List[Tuple[int, List[int]]]:
    """
    Sample generator for generating arrays of int
    """
    for size in SIZES:

        sample = [random.randint(LOWER, UPPER) for _ in range(size)]
        
        yield size, sample


def generate_strings() -> List[Tuple[int, List[int]]]:

    for size in SIZES:

        chars = [random.choice(string.printable) for _ in range(size)]
        sample = "".join(chars)
        
        yield size, sample
