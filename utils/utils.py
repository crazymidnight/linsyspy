import re
import matplotlib.pyplot as plt
import numpy as np
import termcolor


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
    x_history = []
    y_history = []

    for i in range(int(t[0])):
        print(f'Iteration #{i + 1}:')
        y = np.matmul(c, x) + np.matmul(d, u) + np.matmul(f, n)
        y_history.append(y[0])
        x = np.matmul(a, x) + np.matmul(b, u) + np.matmul(e, n)
        x_history.append(x[0])
        n = np.random.normal(size=(len(n), 1))
        print(f' X = {x.transpose()}\n', f'Y = {y.transpose()}')

    plt.plot(x_history, y_history)
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


def quality(a, b, c, d, u, x):
    """calculating quality indicators: transient time, overshoot, static error"""
    y_history = []
    t = [i for i in range(201)]
    u = np.ones(shape=u.shape, dtype=float)
    x = np.zeros(shape=x.shape, dtype=float)
    y_history.append(0)
    transient_time = None
    for i in range(200):
        print(f'Iteration #{i + 1}:')
        y = np.matmul(c, x) + np.matmul(d, u)
        y_history.append(y[0])
        x = np.matmul(a, x) + np.matmul(b, u)
        print(f' X = {x.transpose()}\n', f'Y = {y.transpose()}')
    for idx, i in enumerate(y_history):
        if np.abs(i) > 0.95 * np.abs(y_history[199]) and np.abs(i) < 1.05 * np.abs(y_history[199]):
            transient_time = idx + 1
            break
    overshoot = (np.max(np.abs(y_history)) - np.abs(y_history[199])) / np.abs(y_history[199]) * 100
    plt.plot(t, y_history)
    plt.show()
    print(termcolor.colored(f'Overshutting: {round(overshoot[0], 2)}%', 'green'))
    print(termcolor.colored(f'Transient time: {transient_time} s', 'green'))

if __name__ == '__main__':
    path = '../input.txt'

    A, B, C, D, E, F, X, U, N, Y, T = build_model(path)
    quality(A, B, C, D, U, X)

