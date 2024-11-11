import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from allocations import balls_and_bins, max_gap, strat
    

def expspace(start: float, stop: float, num: int):
    return np.exp(np.linspace(np.log(start), np.log(stop), num))


T = 20 # samples per experiment
m = 100 # bins
n_list_lin = np.int64(np.linspace(m**0.5, m**2, 16))
n_list_exp = np.int64(   expspace(m**0.5, m**2, 16))
n_list = sorted({m}.union(n_list_lin).union(n_list_exp)) # balls
d_list = [1, 1.25, 1.5, 1.75, 2, 3] # preselected beans
b_list = [1, 20, 100, 1000, 2000, 5000] # batch size
#b_list = sorted({1}.union(np.int64(np.linspace(m, m*m, 6)))) # batch size

def strategy_list(d:float):
    return [strat.Compare, strat.Median, strat.Quartile] if d > 1 else [strat.Null]

def log(d, s, n):
    s_list = strategy_list(d)
    di = d_list.index(d)
    si = s_list.index(s)
    ni = n_list.index(n)
    dl = len(d_list)
    sl = len(s_list)
    nl = len(n_list)
    progress = (di + (si + ni/nl)/sl)/dl
    percent = round(progress*100)
    print(percent*'#' + (100-percent)*'-' + f' {percent}%  d({di+1}/{dl}) s({si+1}/{sl}) n({ni+1}/{nl})', end='\r')


data = []

for d in d_list:
    for strategy in strategy_list(d):
        for n in n_list:
            log(d, strategy, n)
            for b in filter(lambda b: b <= n, b_list):
                gaps = [
                    max_gap(balls_and_bins(n, m, d, b, strategy), n/m)
                    for _ in range(T)
                ]
                mean_gap = np.mean(gaps)
                std_gap = np.std(gaps)
                data.append((n, m, d, b, strategy.name, mean_gap, std_gap))

print()
df = pd.DataFrame(data, columns=["n", "m", "d", "b", "strategy", "mean_gap", "std_gap"])
print('saving...')

df.to_csv('data.csv', index=False)

'''
LOG = True
NORM = True 

    x = n_list
    y = np.array(mean_gaps)
    if NORM:
        x = x/m # x = n/m
        y = y/x # y = (max gap)/(n/m)
    plt.plot(x, y, label=f'd = {d}')
plt.legend()

if not NORM:
    plt.xlabel('$n$')
    plt.ylabel('$G_n$')
else:
    plt.xlabel('$n/m$')
    plt.ylabel(r'$\frac{G_n}{n/m}$', rotation=0)

if LOG:
    plt.xscale('log')
    plt.yscale('log')
plt.show()

'''