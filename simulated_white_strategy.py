import numpy as np
import matplotlib.pyplot as plt
from torch import where

def generate_season_scores(n: int):
    return np.random.uniform(low = 0, high = 1, size = n)

def generate_barrier():
    return np.random.uniform(low = 0, high = 1, size = 1)[0]

def white_wins(whites, blacks):
    if whites > blacks:
        return True
    else:
        return False

def one_case(first_decision, barrier, n):
    X = generate_season_scores(n)

    whites_result = X[first_decision-1]

    for_black = np.array(X[first_decision:])
    powers = list(range(len(for_black), 0, -1))

    raised = np.power(1 - np.abs(for_black - barrier), powers)

    try:
        b = np.where(raised > whites_result)[0][0]
        return('bb', for_black[b])
    except:
        try:
            b = np.where(for_black > whites_result)[0][0]
            return('bs', for_black[b])
        except:
            return('w', whites_result)

dict_white = {k: [] for k in range(2, 100)}
dict_black_standard = {k: [] for k in range(2, 100)}
dict_black_barrier = {k: [] for k in range(2, 100)}

for b in [0.5]:
    for i in range(1000):
        for j in range(2, 100):
            print(b, i, j)
            x = one_case(100 - j + 1, b, 100)
            if x[0] == 'w':
                dict_white[j].append(x[1])
            elif x[0] == 'bb':
                dict_black_barrier[j].append(x[1])
            else:
                dict_black_standard[j].append(x[1])

ns = list(range(2, 100))
vals_white = []
vals_black_barrier = []
vals_black_standard = []

for i in ns:
    val_list = dict_white[i]
    val = np.quantile(val_list, 0.5)
    vals_white.append(val)

    val_list = dict_black_barrier[i]
    val = np.quantile(val_list, 0.5)
    vals_black_barrier.append(val)

    val_list = dict_black_standard[i]
    val = np.quantile(val_list, 0.5)
    vals_black_standard.append(val)

plt.scatter(ns, vals_white)
plt.scatter(ns, vals_black_barrier)
plt.scatter(ns, vals_black_standard)
plt.show()