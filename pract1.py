# def print_prime(n:int) -> list:
#     """
#     Print list of prime numbers from the range of numbers given
    
#     :param n: Range of number
#     :type n: int
#     :return: List of prime numbers from range
#     :rtype: list
#     """
#     prime_n = []
#     for _ in range(2,n+1):
#         # print(_)
#         for i in range(2,_+1):
#             # print(f"{_} and {i}")
#             if i < _:
#                 # print("inside")
#                 if _%i == 0:
#                     # print(f"{_} not prime")
#                     break
#             else:
#                 # print(f"{_} is prime")
#                 prime_n.append(_)
#     # print(prime_n)
#     return prime_n
def print_prime(n:int) -> list:
    """
    Print list of prime numbers from the range of numbers given
    
    :param n: Range of number
    :type n: int
    :return: List of prime numbers from range
    :rtype: list
    """
    primes = [True] * (n + 1)
    print(primes)

    # 0 and 1 are not prime
    primes[0], primes[1] = False, False
    print(primes)
    print(f"range is {int(n ** 0.5) + 1}")
    for i in range(2, int(n ** 0.5) + 1):
        print(f"i is {i}")
        if primes[i]:
            for j in range(i * i, n + 1, i):
                print(f"j is {j}")
                primes[j] = False

    res = [i for i in range(1, n + 1) if primes[i]]
    # print(f"res is {res}")
    # print(res if res else "No")
    return res
print(print_prime(20))
