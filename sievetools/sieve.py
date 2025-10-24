'''
this is my apple
'''
import sys
import math
import numpy as np



def sieve_slow(nmax):
    """
    Function to compute prime numbers. 
    
    Arguments: 
        - nmax: integer. Upper bound for prime search.

    Ourputs:
        - all_primes: list. List with all the prime numbers slower than nmax
    
    """

    all_primes = []
    if max==1:
        return []
    if nmax == 2: 
        all_primes = [2]
    else:
        primes_head = [2]
        first = 3
        primes_tail = np.arange(first,nmax+1,2)
        while first <= round(math.sqrt(primes_tail[-1])):
            first = primes_tail[0]
            primes_head.append(first)
            non_primes = first * primes_tail
            primes_tail = np.array([ n for n in primes_tail[1:]
                                    if n not in non_primes ])

    all_primes = primes_head + primes_tail.tolist()
    
    return all_primes



def sieve_fast(nmax):
    """
    Function to compute prime numbers in a more efficient way than sieve_slow()
    
    Arguments: 
        - nmax: integer. Upper bound for prime search.

    Ourputs:
        - all_primes: list. List with all the prime numbers slower than nmax   
    
    """
    
    all_primes = []

    if nmax == 2: 
        all_primes = [2]

    else:

        primes_head = [2]
        first = 3

        # The primes tail will be kept both as a set and as a sorted list
        primes_tail_lst = range(first,nmax+1,2)
        primes_tail_set = set(primes_tail_lst)

        # Now do the actual sieve
        while first <= round(math.sqrt(primes_tail_lst[-1])):
            # Move the first leftover prime from the set to the head list
            first = primes_tail_lst[0]
            primes_tail_set.remove(first)  # remove it from the set
            primes_head.append(first) # and store it in the head list

            # Now, remove from the primes tail all non-primes.  For us to be able
            # to break as soon as a key is not found, it's crucial that the tail
            # list is always sorted.
            for next_candidate in primes_tail_lst:
                try:
                    primes_tail_set.remove(first * next_candidate)
                except KeyError:
                    break

            # Build a new sorted tail list with the leftover keys
            primes_tail_lst = list(primes_tail_set)
            primes_tail_lst.sort()

        all_primes = primes_head + primes_tail_lst

    return all_primes



def get_primes(nmax, method):
    """
    Function to run different algorithms for prime numbers
    """
    
    if method == "slow":
        return sieve_slow(nmax)
    elif method == "fast":
        return sieve_fast(nmax)
    else:
        raise NotImplementedError()
        
        
        
def proportion_primes(nmin, nmax, step=100):
    """
    Function to compute proportion of prime numbers
    
    Arguments:
        - nmin: integer. Minimun number
        - nmax: integer. Maximum number
        - step: integer. Stepsize for the prime search.
    
    Outputs:
        - all_n: list. All integers used for the search.
        - all_proportions: list. Result of proportions of primes per each number in all_n
        
    """
    
    all_n = np.arange(nmin, nmax, step).astype(int)
    all_proportions = []
    
    for n in all_n:
        all_primes = get_primes(n, method="fast")
        all_proportions.append(len(all_primes) / n)
        
    return all_n, all_proportions