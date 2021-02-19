# Program to multiply two matrices using nested loops
import random
import numpy as np

N = 250

@profile
def create_random_matrix(i, j):
    M = []
    for i in range(i):
        M.append([random.randint(0,100) for r in range(j)])
    return M

@profile
def create_zero_matrix(i, j):
    M = []
    for i in range(i):
        M.append([0] * (j))
    return M

# NxN matrix
X = create_random_matrix(N, N)

# Nx(N+1) matrix
Y = create_random_matrix(N, N+1)

# result is Nx(N+1)
result = create_zero_matrix(N, N+1)

@profile
def matmult(X, Y, result):
    # iterate through rows of X
    for i in range(len(X)):
        # iterate through columns of Y
        for j in range(len(Y[0])):
            # iterate through rows of Y
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
    return result 

@profile
def numpy_matmult(X,Y):
    return np.matmul(X, Y)

result = matmult(X, Y, result)
result_numpy = numpy_matmult(X, Y)

@profile
def print_result(result):
    for r in result:
        print(r)

print_result(result)