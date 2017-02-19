from gcd import gcd
import random


def relative_prime(n):
    if n <= 0:
        return
    if n == 1:
        return 1
    rel_prime = random.randrange(1, n//2 + 1)
    while gcd(rel_prime, n) != 1:
        rel_prime += 1
    return rel_prime


def test():
    assert relative_prime(0)  is None
    assert relative_prime(-1) is None
    assert relative_prime(1)  == 1

    for i in range(100):
        n = random.randrange(10, 10**6)
        assert gcd(relative_prime(n), n) == 1

if __name__ == '__main__':
    test()
    print('test pass')
