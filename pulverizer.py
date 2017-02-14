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
