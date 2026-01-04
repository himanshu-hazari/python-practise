from sre_constants import ASSERT_NOT
from pract1 import print_prime

def test_prime_number():
    assert print_prime(2) == [1,2]

def test_no_prime_number():
    assert print_prime(5) == [1,2,3,5]