import sieve

# test 3 - there are 10 primes less than 30
count = 0
gen = sieve.primes()
while gen.next() < 30:
    count += 1

assert count == 10

