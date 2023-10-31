import math

def is_prime(n):
    """
    Determines if a given number is a prime number.

    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

    Args:
        n (int): The number to be checked for primality.

    Returns:
        bool: True if 'n' is a prime number, False otherwise.

    Example:
        >>> is_prime(5)
        True
        >>> is_prime(4)
        False
    """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
