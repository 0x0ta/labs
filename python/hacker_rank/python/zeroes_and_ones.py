import numpy

dimensions_array = tuple(map(int, input().split()))

print(numpy.zeros((dimensions_array), dtype=numpy.int))
print(numpy.ones((dimensions_array), dtype=numpy.int))
