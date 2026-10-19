
def prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def prime_till_n(n):
    print("Prime numbers till", n, "are:")
    for i in range(2, n + 1):
        if prime(i):
            print(i, end=" ")
    print()


def first_n_prime(n):
    count = 0
    num = 2
    print("First", n, "prime numbers are:")
    while count < n:
        if prime(num):
            print(num, end=" ")
            count += 1
        num += 1
    print()


n = int(input("Enter a number: "))

# (a) Check whether n is prime
if prime(n):
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")

# (b) Generate prime numbers till n
prime_till_n(n)

# (c) Generate first n prime numbers
first_n_prime(n)
