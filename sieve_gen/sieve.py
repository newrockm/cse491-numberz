# an implementation of Eratosthenes' Sieve as a generator

def _is_prime(primes, n):
    for i in primes:
        if n % i == 0:
            return False
    return True

def primes():
    # first iteration, return 2 as the first prime number
    primeslist = [2]
    yield 2

    # subsequent iterations build off of previously determined primes
    start = primeslist[-1] + 1
    while 1:
        if _is_prime(primeslist, start):
            primeslist.append(start)
            yield start

        start += 1

