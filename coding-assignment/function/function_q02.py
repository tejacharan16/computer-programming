def check_prime(n):
    """
    Problem 2: Write a function to check if a number is prime.
    Input: n = 11
    Output: True
    Explanation: 11 is a prime number because it has no divisors other than 1 and itself.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True