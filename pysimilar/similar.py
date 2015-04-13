#!/usr/bin/env python
from math import pow
from decimal import Decimal

# TODO: Look at these -> http://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.pdist.html

def _nth_root(value, n_root):
    """ Computes the nth-root of the value. """
    return value ** (1 / n_root)

def _square_rooted(x):
    """ Computes the square root of the list. """
    return sqrt(sum([(a * a) for a in x]))
    
def dice_similarity(a, b):
    """ Calculates the Sørensen–Dice coefficient. 
    
    This is very similar to the Jaccard Similarity, but uses twice the weigthing
    for to agreements in the set.
    
    It can be explained as: D(A,B) = 2 |A and B | / (|A|+|B|)
    """
    if not len(a) or not len(b): return 0.0
    """ quick case for true duplicates """
    if a == b: return 1.0
    """ if a != b, and a or b are single chars, then they can't possibly match """
    if len(a) == 1 or len(b) == 1: return 0.0
 
    """ use python list comprehension, preferred over list.append() """
    a_bigram_list = [a[i:i+2] for i in range(len(a)-1)]
    b_bigram_list = [b[i:i+2] for i in range(len(b)-1)]
 
    a_bigram_list.sort()
    b_bigram_list.sort()
 
    # assignments to save function calls
    lena = len(a_bigram_list)
    lenb = len(b_bigram_list)
    # initialize match counters
    matches = i = j = 0
    while (i < lena and j < lenb):
        if a_bigram_list[i] == b_bigram_list[j]:
            matches += 2
            i += 1
            j += 1
        elif a_bigram_list[i] < b_bigram_list[j]:
            i += 1
        else:
            j += 1
 
    score = float(matches)/float(lena + lenb)
    return score

def jaccard_similarity(x, y):
    """ Returns the Jaccard Similarity Coefficient (Jarccard Index) between two 
    lists. 
    
    From http://en.wikipedia.org/wiki/Jaccard_index: The Jaccard
    coefficient measures similarity between finite sample sets, as is defined as
    the size of the intersection divided by the size of the union of the sample
    sets.
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

def euclidean_distance(self,x,y):
    """ Return the Euclidean distance between two lists.
    """
    return sqrt(sum(pow(a - b, 2) for a, b in zip(x, y)))

def manhattan_distance(x, y):
    """ Returns the Manhattan (City Block) distance between two lists
    """
    return sum(abs(a - b) for a, b in zip(x, y))

def minkowski_distance(x, y, p_value):
    """ Returns the Minkowski distance between two lists.
    """
    return _nth_root(sum(pow(abs(a - b), p_value) for a, b in zip(x, y)), p_value)


