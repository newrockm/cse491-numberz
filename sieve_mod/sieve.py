# an implementation of Eratosthenes' Sieve in a module

_primeslist = []

def _is_prime(primes, n):
    for i in primes:
        if n % i == 0:
            return False
    return True

def next():
    # first iteration, add 2 as a prime number
    if len(_primeslist) == 0:
        _primeslist.append(2)
        return 2

    # subsequent iterations build off of the previously determined list
    start = _primeslist[-1] + 1
    while 1:
        if _is_prime(_primeslist, start):
            _primeslist.append(start)
            return start

        start += 1

