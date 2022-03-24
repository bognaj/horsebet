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

    raised = np.power(for_black, powers)

    try:
        b = np.where(raised > whites_result)[0][0]
        return('b', None)
    except:
        try:
            b = np.where(for_black > whites_result)[0][0]
            return('b', None)
        except:
            return('w', whites_result)

dict_06 = {k: [] for k in range(2, 100)}

for b in [0.999]:
    for i in range(1000):
        for j in range(2, 100):
            print(b, i, j)
            x = one_case(100 - j + 1, b, 100)
            if x[0] == 'w':
                dict_06[j].append(x[1])

ns = list(range(2, 100))
vals = []

for i in ns:
    val_list = dict_06[i]
    val = np.quantile(val_list, 0.5)
    vals.append(val)


plt.scatter(ns, vals)
plt.show()