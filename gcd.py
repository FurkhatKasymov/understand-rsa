def gcd(a, b):
    while b != 0:
        r = a%b
        a = b
        b = r
    return a


def test():
    assert gcd(0, 1234) == 1234, "everything devides 0"
    assert gcd(3, 5) == 1, "3 and 5 are relatively prime numbers"
    assert gcd(81, 27) == 27, "27 devides 81"
    assert gcd(16, 24) == 8

if __name__ == '__main__':
    test()
    print('test pass')
