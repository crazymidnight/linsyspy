import re
import matplotlib.pyplot as plt
import numpy as np


def open_file(path):
    """downloading data"""
    file = open(path, 'r')
    input_data = file.read()
    file.close()
    return input_data


def find_numbers(raw_numbers):
    """searching numbers"""
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
    """searching arrays"""
    arrays = []
    raw_arrays = re.split(r']', data)

    for raw_array in raw_arrays:
        raw_numbers = re.split(r',', raw_array)
        numbers = find_numbers(raw_numbers)
        if len(numbers) > 0:
            arrays.append(numbers)

    return arrays


def build_model(path):
    """building model"""
    input_data = open_file(path)
    arrays = find_array(input_data)
    arrays = np.array(arrays)
    x, u, n, y, t = arrays

    x = np.reshape(x, newshape=(len(x), 1))
    u = np.reshape(u, newshape=(len(u), 1))
    n = np.reshape(n, newshape=(len(n), 1))
    y = np.reshape(y, newshape=(len(y), 1))

    a = np.random.uniform(low=-0.5, high=0.5, size=(len(x), len(x)))
    b = np.random.uniform(low=-0.5, high=0.5, size=(len(x), len(u)))
    c = np.random.uniform(low=-0.5, high=0.5, size=(len(y), len(x)))
    d = np.random.uniform(low=-0.5, high=0.5, size=(len(y), len(u)))
    e = np.random.uniform(low=-0.5, high=0.5, size=(len(x), len(n)))
    f = np.random.uniform(low=-0.5, high=0.5, size=(len(y), len(n)))

    return a, b, c, d, e, f, x, u, n, y, t


def calculate_model(a, b, c, d, e, f, x, u, n, y, t):
    X_history = []
    Y_history = []

    for i in range(int(t[0])):
        print(f'Iteration #{i + 1}:')
        y = np.matmul(c, x) + np.matmul(d, u) + np.matmul(f, n)
        Y_history.append(y[0])
        x = np.matmul(a, x) + np.matmul(b, u) + np.matmul(e, n)
        X_history.append(x[0])
        n = np.random.normal(size=(len(n), 1))
        print(f' X = {x.transpose()}\n', f'Y = {y.transpose()}')

    plt.plot(X_history, Y_history)
    plt.show()


def stability(input_a):
    eigval_a = np.linalg.eigvals(input_a)

    for a in eigval_a:
        if abs(a) < 1:
            continue
        elif abs(a) == 1:
            return 'System is neutral'
        else:
            stable = False
            return 'System is unstable'
    return 'System is stable'