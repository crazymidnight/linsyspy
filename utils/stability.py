import numpy as np

def stability(A):
    eA = np.linalg.eigvals(A)

    for a in eA:
        if abs(a) < 1:
            continue
        elif abs(a) == 1:
            return 'System is neutral'
        else:
            stable = False
            return 'System is unstable'
    return 'System is stable'
