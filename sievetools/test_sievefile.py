from sievetools import *
import pytest


def test_sievefast_one():
    sievefast_one = sieve_fast(1)
    assert sievefast_one==[]


def test sievefast lessone():
    with pytest.raises(ValueError):
        sieve_ fast (-10).

def test_sievefast_interior():
    primes = sieve_fast (55)
    true_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
    assert primes == true_primes

    