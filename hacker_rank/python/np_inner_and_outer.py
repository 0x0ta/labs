import numpy

A = numpy.array([input().split()], dtype=int)
B = numpy.array([input().split()], dtype=int)

print(numpy.inner(A, B)[0][0])
print(numpy.outer(A, B))

