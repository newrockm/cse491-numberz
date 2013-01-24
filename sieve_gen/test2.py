import sieve

# test 2 - the fourth prime should be 7 - happy :)
gen = sieve.primes()
gen.next()
gen.next()
gen.next()
assert gen.next() == 7

