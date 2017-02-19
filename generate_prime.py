import math
import random


def generate_prime():
    lower = 10**6
    upper = 10**9
    n = random.randrange(lower, upper)
    while not is_prime(n):
        n += 1
    return n

def is_prime(n):
    if n < 2:
        return False
    if fails_fermats_test(n):
        return False
    for i in range(2, int(math.ceil(math.sqrt(n)))):
        if n%i == 0:
            return False
    return True

def fails_fermats_test(n):
    return ((2 << (n - 2)) - 2) & 1


def test():
    assert is_prime(2)
    assert is_prime(31)
    assert is_prime(179424779)

    assert not is_prime(1)
    assert not is_prime(34)
    assert not is_prime(12121227)
    
    
    for i in range(10):
        assert is_prime(generate_prime())

if __name__ == '__main__':
    test()
    print('test pass')
