from typing import List, Optional

# These functions allow to estimate time complexity of tested function

def linear(array: List[int]) -> None:
    
    res = 0
    for a in array:
        res += a


def quadratic(array: List[int]) -> None:

    res = 1

    for a in array:
        for b in array:
            res += a

def cubic(array: List[int]) -> None:

    res = 0
    for a in array:
        for b in array:
            for c in array:
                res += c

    return c
