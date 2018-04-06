from utils import utils
import matplotlib.pyplot as plt
import termcolor


path = 'input.txt'
A, B, C, D, E, F, X, U, N, Y, T = utils.build_model(path)
print(termcolor.colored(utils.stability(A), 'blue'))
x_history, y_history = utils.calculate_model(A, B, C, D, E, F, X, U, N, Y, T, non_stationary=False)
utils.quality(A, B, C, D, U, X, N,
              non_stationary=False)
cleaned_x = utils.median_filter(x_history)
cleaned_y = utils.median_filter(y_history)
plt.plot(cleaned_x, cleaned_y)
plt.show()
