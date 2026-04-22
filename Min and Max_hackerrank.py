import numpy
n, m = map(int, input().split())
array = numpy.array([input().split() for _ in range(n)], int)
min_axis_1 = numpy.min(array, axis=1)
print(numpy.max(min_axis_1))
