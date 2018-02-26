import control
from utils import get_data

path = 'input.txt'

A, B, C, D, E, F, X, U, N, Y, T = get_data.build_model(path)
system = control.ss(A, B, C, D)

print(control.stability_margins(system))