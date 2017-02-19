def raise_with_modulo(number, power, base):
    if power < 0:
        return
    result = 1
    while power > 0:
        if is_even(power):
            number = (number * number) % base
            power //= 2
        else:
            result = (result * number) % base
            power -= 1
    return result % base

def is_even(n): return n & 1 == 0


def test():
    assert raise_with_modulo(1, -1, 1)      == None
    assert raise_with_modulo(1, 0, 1)       == 0

    # test fast exponentiation
    assert raise_with_modulo(2, 4, 17)      == 16
    assert raise_with_modulo(2, 5, 33)      == 32

    # random test with modulo
    import random
    rand = lambda: random.randrange(1000)
    for i in range(100):
        a, b, c = rand(), rand(), rand()
        assert raise_with_modulo(a, b, c) == (a ** b) % c, "raise_with_modulo(%s, %s, %s) failed." % (a, b, c)
    

if __name__ == '__main__':
    test()
    print('test pass')
