import re

import matplotlib.pyplot as plt
import numpy as np


file = open('input.txt', 'r')
input_data = file.read()
file.close()
print(input_data)


def find_numbers(raw_numbers):
    """функция поиска чисел"""
    numbers = []

    for raw_number in raw_numbers:
        digits = re.findall(r'[\d.-]', raw_number)

        if len(digits) > 0:
            number = ''

            for digit in digits:
                number += digit

            numbers.append(float(number))

    return numbers


def find_array(data):
    """функция поиска векторов"""
    arrays = []
    raw_arrays = re.split(r']', data)

    for raw_array in raw_arrays:
        raw_numbers = re.split(r',', raw_array)
        numbers = find_numbers(raw_numbers)
        if len(numbers) > 0:
            arrays.append(numbers)

    return arrays

arrays = find_array(input_data)
arrays = np.array(arrays)
X, U, N, Y, T = arrays

X = np.reshape(X, newshape=(len(X), 1))
U = np.reshape(U, newshape=(len(U), 1))
N = np.reshape(N, newshape=(len(N), 1))
Y = np.reshape(Y, newshape=(len(Y), 1))

A = np.random.normal(size=(len(X), len(X)))
B = np.random.normal(size=(len(X), len(U)))
C = np.random.normal(size=(len(Y), len(X)))
D = np.random.normal(size=(len(Y), len(U)))
E = np.random.normal(size=(len(X), len(N)))
F = np.random.normal(size=(len(Y), len(N)))


X_history = []
Y_history = []


for i in range(int(T[0])):
    print(f'Iteration #{i + 1}:')
    X = np.matmul(A, X) + np.matmul(B, U) + np.matmul(E, N)
    X_history.append(X[0])
    Y = np.matmul(C, X) + np.matmul(D, U) + np.matmul(F, N)
    Y_history.append(Y[0])
    N = np.random.normal(size=(len(N), 1))
    print(f' X = {X.transpose()}\n', f'Y = {Y.transpose()}')


plt.plot(X_history, Y_history)
plt.show()