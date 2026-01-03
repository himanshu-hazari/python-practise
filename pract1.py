#Simple loop test
#check prime or not
from math import sqrt


def print_prime(n:int) -> list:
    prime_n = [1]
    for _ in range(1,n+1):
        # print(_)
        for i in range(1,_+1):
            # print(f"{_} and {i}")
            if i == 1:
                continue
            elif i < _:
                # print("inside")
                if _%i == 0:
                    # print(f"{_} not prime")
                    break
            else:
                # print(f"{_} is prime")
                prime_n.append(_)
    # print(prime_n)
    return prime_n

print(print_prime(5))