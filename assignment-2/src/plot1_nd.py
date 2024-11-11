import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('data.csv')

'''
n
m = 100
d
b = 1
strategy = cmp, na
mean_gap
std_gap
'''

m = 100

df_filtered = df[(df['m'] == m) & (df['b'] == 1) & ((df['strategy'] == 'cmp') | (df['strategy'] == 'na'))]

for NORM in (False, True):
    for LOG in (False, True):
        for d, df_d in df_filtered.groupby('d'):
            df_d_sorted = df_d.sort_values(by='n')

            x = np.array(df_d_sorted['n'])
            y = np.array(df_d_sorted['mean_gap'])

            if NORM:
                x = x/m # x = n/m
                y = y/x # y = mean_gap/(n/m)
            plt.plot(x, y, label=f'd = {d}')

        if not NORM:
            plt.xlabel('$n$')
            plt.ylabel('$G_n$', rotation=0)
        else:
            plt.xlabel('$n/m$')
            plt.ylabel(r'$\frac{G_n}{n/m}$', rotation=0)

        if LOG:
            plt.xscale('log')
            plt.yscale('log')

        plt.legend()
        #plt.show()
        plt.savefig('plots/plot1_nd'  + ('_norm' if NORM else '') + ('_log' if LOG else '') + '.png')
        plt.clf()

pass

