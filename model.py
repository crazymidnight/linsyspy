from utils import utils

path = 'input.txt'

A, B, C, D, E, F, X, U, N, Y, T = utils.build_model(path)

print(utils.stability(A))

utils.calculate_model(A, B, C, D, E, F, X, U, N, Y, T)

utils.quality(A, B, C, D, U, X)

utils.median_filter(X)  