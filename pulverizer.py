from numpy import array


def pulverizer(a, b):
    X = array([1, 0])
    Y = array([0, 1])
    while b != 0:
        R = X - a//b*Y
        X = Y
        Y = R
        t = a; a = b; b = t % b
    return X.tolist()


def test():
    assert pulverizer(0, 10) == [0,  1], "GCD is 10"
    assert pulverizer(10, 0) == [1,  0], "GCD is 10"
    assert pulverizer(3, 5)  == [2, -1], "3 and 5 relatively prime eg GCD is 1"
    assert pulverizer(12, 8) == [1, -1], "GCD is 4"
    assert pulverizer(1, 10) == [1,  0], "GCD is 1"

if __name__ == '__main__':
    test()
    print('test pass')
