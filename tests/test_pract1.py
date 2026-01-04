from pract1 import print_prime

def test_prime_number():
    """
    Check prime number 
    """
    assert print_prime(2) == [1,2]

def test_no_prime_number():
    """
    Check prime number 
    """
    assert print_prime(5) == [1,2,3,5]
