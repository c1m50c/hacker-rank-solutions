# https://www.hackerrank.com/challenges/np-inner-and-outer/problem #

import numpy

a = numpy.array([list(map(int, input().split()))])
b = numpy.array([list(map(int, input().split()))])

print(numpy.inner(a, b)[0][0])
print(numpy.outer(a, b))