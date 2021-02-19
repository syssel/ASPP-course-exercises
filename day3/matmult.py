# Program to multiply two matrices using nested loops
import random
import numpy as np

N = 250

@profile
def create_random_matrix(i, j):
    return np.random.randint(0, 100, (i,j))

@profile
def create_zero_matrix(i, j):
    return np.zeros((i,j))

# NxN matrix
X = create_random_matrix(N, N)

# Nx(N+1) matrix
Y = create_random_matrix(N, N+1)

# result is Nx(N+1)
result = create_zero_matrix(N, N+1)

@profile
def numpy_matmult(X,Y):
    return np.matmul(X, Y)

result_numpy = numpy_matmult(X, Y)

@profile
def print_result(result):
    for r in result:
        print(r)

print_result(result)