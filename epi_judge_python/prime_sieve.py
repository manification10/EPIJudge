from typing import List

from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    isPrime = [True]*(n+1)
    isPrime[0] = False
    isPrime[1] = False
    primes = []

    for i in range(2, n+1):
        if isPrime[i] == True:
            primes.append(i)
            # seive
            for j in range(i+i, n+1, i):
                isPrime[j] = False

    return primes


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
