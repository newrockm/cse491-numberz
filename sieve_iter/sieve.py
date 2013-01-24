# an implementation of Eratosthenes' Sieve as an iterator

class primes(object):
    def __init__(self):
        self.primeslist = []

    def __iter__(self):
        return self

    def _is_prime(self, n):
        for i in self.primeslist:
            if n % i == 0:
                return False
        return True

    def next(self):
        if len(self.primeslist) == 0:
            self.primeslist.append(2)
            return 2

        self.start = self.primeslist[-1] + 1
        while 1:
            if self._is_prime(self.start):
                self.primeslist.append(self.start)
                return self.start
            self.start += 1

