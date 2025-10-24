import time
import matplotlib.pyplot as plt
import numpy as np

from .sieve import sieve_slow, sieve_fast


def time_rng(fun, nrange, verbose=False):
    """
    Time a function over a range of parameters.

    Returns the list of run times.

    The function should be callable with a single argument: it will be
    called with each entry from nrange in turn.

    If verbose is true, at each step the value of nrange and time for the
    call is printed.
    """

    times = []
    for n in nrange:
        t0 = time.perf_counter()
        fun(n)
        t = time.perf_counter() - t0
        if verbose:
            print(n, t)
        times.append(t)

    return nrange, times


def time_sieves():
    "simple timing demo"

    rng = np.linspace(1000, 5000, 20).astype(int)
    plt.figure()
    plt.title('Sieve of Erathostenes')
    plt.xlabel('Size')
    plt.ylabel('t(s)')
    
    # END SOLUTION

    plt.plot(rng, time_rng(sieve_fast, rng)[1], label="Sieve Fast")
    plt.plot(rng, time_rng(sieve_slow, rng)[1], label="Sieve Slow")

    plt.legend()
    plt.show()