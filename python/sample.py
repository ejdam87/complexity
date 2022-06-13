from typing import List

# This is a sample funtion with time complexity of O(n); n is length of array
def maximum(array: List[int]) -> int:
    
    mx = array[0]

    for i in range(1, len(array)):

        if array[i] > mx:
            mx = array[i]

    return mx


def is_palindrome(word: str) -> bool:
    
    return word == word[::-1]


def string_sum(string: str) -> int:

    total = 0

    for char in string:
        total += ord(char)
