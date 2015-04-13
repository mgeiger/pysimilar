#!/usr/bin/env python
from math import pow
from decimal import Decimal

# TODO: Look at these -> http://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.pdist.html

def _nth_root(value, n_root):
    return value ** (1 / n_root)

def _square_rooted(x):
    return round(sqrt(sum([(a * a) for a in x])), 3)
    
def euclidean_distance(self,x,y):
    """ Return the Euclidean distance between two lists.
    """
    return sqrt(sum(pow(a - b, 2) for a, b in zip(x, y)))

def jaccard_similarity(x, y):
    """ Returns the Jaccard Similarity between two lists.
    """
    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    union_cardinality = len(set.union(*[set(x), set(y)]))
    return intersection_cardinality / float(union_cardinality)

def cosine_similarity(x,y):
    """ Calculates the Consine Similarity between two lists.
    This will find the normalized dot product of the two attributes
    """
    numerator = sum(a * b for a, b in zip(x, y))
    denominator = _square_rooted(x) * _square_rooted(y)
    return numerator / float(denominator)

def manhattan_distance(x, y):
    """ Returns the Manhattan (City Block) distance between two lists
    """
    return sum(abs(a - b) for a, b in zip(x, y))

def minkowski_distance(x, y, p_value):
    """ Returns the Minkowski distance between two lists.
    """
    return _nth_root(sum(pow(abs(a - b), p_value) for a, b in zip(x, y)), p_value)


