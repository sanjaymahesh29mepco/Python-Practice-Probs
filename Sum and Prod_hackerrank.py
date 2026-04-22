import numpy
n, m = map(int, input().split())
my_array = numpy.array([input().split() for _ in range(n)], int)
sum_result = numpy.sum(my_array, axis=0)
print(numpy.prod(sum_result))
