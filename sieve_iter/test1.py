import sieve

# test 1 - the first prime should be 2
gen = sieve.primes()
assert gen.next() == 2

