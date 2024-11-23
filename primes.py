def sieve_of_eratosthenes(limit):
    """Returns a list of all prime numbers up to a given limit."""
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

    for num in range(2, limit + 1):
        if is_prime[num]:
            primes.append(num)
            for multiple in range(num * num, limit + 1, num):
                is_prime[multiple] = False

    return primes

# Generate prime numbers up to 10,000
primes_up_to_10000 = sieve_of_eratosthenes(10000)
print(primes_up_to_10000[:], len(primes_up_to_10000)  )# Preview first 10 and total count
