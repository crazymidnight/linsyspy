import numpy as np


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
