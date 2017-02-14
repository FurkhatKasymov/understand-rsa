from pulverizer import pulverizer


assert pulverizer(0, 10) == [0,  1], "GCD is 10"
assert pulverizer(10, 0) == [1,  0], "GCD is 10"
assert pulverizer(3, 5)  == [2, -1], "3 and 5 relatively prime eg GCD is 1"
assert pulverizer(12, 8) == [1, -1], "GCD is 4"
assert pulverizer(1, 10) == [1,  0], "GCD is 1"
