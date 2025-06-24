def is_prime(n):
    if n <= 1:
        print(f"{n} is not a prime number.")
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(f"{n} is not a prime number.")
            return False
    print(f"{n} is a prime number.")
    return True
is_prime(7)
is_prime(10)
