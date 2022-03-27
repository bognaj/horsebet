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

def one_case_classic(first_decision, barrier, n):
    X = generate_season_scores(n)

    whites_result = X[first_decision-1]
    for_black = np.array(X[first_decision:])
    powers = list(range(len(for_black), 0, -1))
    raised =  1 - np.abs(for_black - barrier)

    try:
        b = np.where(raised > whites_result)[0][0]
        return('bb', for_black[b])
    except:
        try:
            b = np.where(for_black > whites_result)[0][0]
            return('bs', for_black[b])
        except:
            return('w', whites_result)


def one_case_all_power(first_decision, barrier, n):
    X = generate_season_scores(n)

    whites_result = X[first_decision-1]
    for_black = np.array(X[first_decision:])
    powers = list(range(len(for_black), 0, -1))
    raised =  np.power(1 - np.abs(for_black - barrier), powers)

    try:
        b = np.where(raised > whites_result)[0][0]
        return('bb', for_black[b])
    except:
        try:
            b = np.where(for_black > whites_result)[0][0]
            return('bs', for_black[b])
        except:
            return('w', whites_result)

def one_case_old(first_decision, barrier, n):
    X = generate_season_scores(n)

    whites_result = X[first_decision-1]
    for_black = np.array(X[first_decision:])
 
    try:
        b = np.where(for_black > whites_result)[0][0]
        return('bs', for_black[b])
    except:
        return('w', whites_result)

dict_classic = {k: [] for k in range(2, 100)}
dict_all_power = {k: [] for k in range(2, 100)}
dict_old= {k: [] for k in range(2, 100)}

for b in [0.5]:
    for i in range(10000):
        for j in range(2, 100):
            print(b, i, j)
            x = one_case_classic(100 - j + 1, b, 100)
            y = one_case_all_power(100 - j + 1, b, 100)
            z = one_case_old(100 - j + 1, b, 100)
            if x[0] == 'w':
                dict_classic[j].append(x[1])
            if y[0] == 'w':
                dict_all_power[j].append(y[1])
            if z[0] == 'w':
                dict_old[j].append(z[1])

                
ns = list(range(2, 100))
classic = []
all_power = []
old = []

for i in ns:
    val_list = dict_classic[i]
    val = np.quantile(val_list, 0.5)
    classic.append(val)

    val_list = dict_all_power[i]
    val = np.quantile(val_list, 0.5)
    all_power.append(val)

    val_list = dict_old[i]
    val = np.quantile(val_list, 0.5)
    old.append(val)


plt.scatter(ns, classic, label = 'classic')
plt.scatter(ns, all_power, label = 'all power')
plt.scatter(ns, old, label = 'old')
#plt.scatter(ns, vals_black_barrier)
#plt.scatter(ns, vals_black_standard)
plt.legend()
plt.show()