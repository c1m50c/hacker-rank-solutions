# https://www.hackerrank.com/challenges/reduce-function/ #
from __future__ import print_function
from fractions import Fraction
import operator

def product(fracs):
    t = reduce(operator.mul, fracs)
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(input()):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)