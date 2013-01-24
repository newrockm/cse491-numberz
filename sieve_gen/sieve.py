# an implementation of Eratosthenes' Sieve as a generator

def _is_prime(primes, n):
    for i in primes:
        if n % i == 0:
            return False
    return True

def primes():
    primeslist = [2]
    start = primeslist[-1] + 1
    while 1:
        if _is_prime(primeslist, start):
            primeslist.append(start)
            yield start

        start += 1

