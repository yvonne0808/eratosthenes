import matplotlib.pyplot as plt

from .sieve import proportion_primes


def plot_sieve(nmin, nmax, log_scale=False):
    """
    Function to plot proportion of prime numbers
    """
    
    all_n, all_proportions = proportion_primes(nmin, nmax)
    plt.plot(all_n, all_proportions)
    plt.xlabel("N")
    plt.ylabel("Proportion of primer numbers")
    if log_scale: 
        plt.xscale("log")
        plt.yscale("log")