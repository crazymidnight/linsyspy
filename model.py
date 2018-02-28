from utils import get_data, stability

path = 'input.txt'

A, B, C, D, E, F, X, U, N, Y, T = get_data.build_model(path)

print(stability.stability(A))

get_data.calculate_model(A, B, C, D, E, F, X, U, N, Y, T)