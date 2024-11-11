import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('data.csv')

'''
n
m = 100
d = 2
b = 1
strategy
mean_gap
std_gap
'''

m = 100

df_filtered = df[(df['m'] == m) & (df['d'] == 2) & (df['b'] == 1)]

for NORM in (False, True):
    for LOG in (False, True):
        for s, df_s in df_filtered.groupby('strategy'):

            df_s_sorted = df_s.sort_values(by='n')

            x = np.array(df_s_sorted['n'])
            y = np.array(df_s_sorted['mean_gap'])

            if NORM:
                x = x/m # x = n/m
                y = y/x # y = mean_gap/(n/m)
            plt.plot(x, y, label={'cmp':'compare', 'med':'median', 'qua':'quartiles'}[s])

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
        plt.savefig('plots/plot3_nk'  + ('_norm' if NORM else '') + ('_log' if LOG else '') + '.png')
        plt.clf()

pass

