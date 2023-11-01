from prime_jc6102 import is_prime
import pytest

def test_is_prime():
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    for num in prime_numbers:
        assert is_prime(num), f"Failed for {num}, expected to be Prime"
