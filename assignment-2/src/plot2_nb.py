import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df1 = pd.read_csv('data_b.csv')
df2 = pd.read_csv('data.csv')
df = pd.concat([df1, df2], ignore_index=True)

'''
n
m = 100
d = 2
b
strategy = cmp, na
mean_gap
std_gap
'''

m = 100

df_filtered = df[(df['m'] == m) & (df['d'] == 2) & ((df['strategy'] == 'cmp') | (df['strategy'] == 'na'))]


for NORM in (False, True):
    for LOG in (False, True):
        for b, df_b in df_filtered.groupby('b'):
            if b not in [1, 20, 100, 1080, 2060, 5000]:
                continue

            df_b_sorted = df_b.sort_values(by='n')

            x = np.array(df_b_sorted['n'])
            y = np.array(df_b_sorted['mean_gap'])

            if NORM:
                x = x/m # x = n/m
                y = y/x # y = mean_gap/(n/m)
            plt.plot(x, y, label=f'b = {b}')

        if not NORM:
            plt.xlabel('$n$')
            plt.ylabel('$G_n$', rotation=0)
        else:
            plt.xlabel('$n/m$')
            plt.ylabel(r'$\frac{G_n}{n/m}$', rotation=0)

        if LOG:
            if NORM: plt.xscale('log')
            plt.yscale('log')

        plt.legend()
        #plt.show()
        plt.savefig('plots/plot2_nb'  + ('_norm' if NORM else '') + ('_log' if LOG else '') + '.png')
        plt.clf()

pass

