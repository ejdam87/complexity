import ctypes
from typing import List

# This file provides united API for C functions (wrapping C function into python one)

def summation(array: List[int]) -> int:

    shared = ctypes.CDLL("C:\\Docs\\Git\\complexity\\c\\sample.so")

    arr = (ctypes.c_int * len(array))(*array)
    n = len(array)
    
    return shared.sum(arr, n)
