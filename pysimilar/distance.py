#!/usr/bin/env python
from math import pow, sqrt
from decimal import Decimal

def _nth_root(value, n_root):
    """ Helper to computer the nth-root of the value. """
    return value ** (1 / n_root)

def _square_rooted(x):
    """ Helper to compute the square root of the list. """
    return sqrt(sum([(a * a) for a in x]))
    
def chebyshev_distance(x1, y1, x2, y2):
    return max(abs(x1 - x2), abs(y1, y2))

def euclidean_distance(x, y):
    """ Return the Euclidean distance between two lists.
    """
    return sqrt(sum(pow(a - b, 2) for a, b in zip(x, y)))
    
def hamming_distance(s1, s2):
    """ Defines the minimum number of substitutions required to change one
    string into another.
    """
    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal lenght.")
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

def manhattan_distance(x, y):
    """ Returns the Manhattan (City Block) distance between two lists
    """
    return sum(abs(a - b) for a, b in zip(x, y))

def minkowski_distance(x, y, p_value):
    """ Returns the Minkowski distance between two lists.
    """
    return _nth_root(sum(pow(abs(a - b), p_value) for a, b in zip(x, y)), p_value)