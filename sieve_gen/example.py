import sieve

count = 1

for n in sieve.primes():
    print n
    count += 1
    if count > 10:
        break

