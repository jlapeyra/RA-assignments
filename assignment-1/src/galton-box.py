import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import sys

def move_left(i, j):
    return (i+1, j)

def move_right(i, j):
    return (i, j+1)

def usage():
    print(f'USAGE:\n\tpython {sys.argv[0]} NUM_STEPS NUM_BALLS')
    exit()

if len(sys.argv) != 3:
    usage()
try:
    NUM_STEPS = int(sys.argv[1])
    NUM_BALLS = int(sys.argv[2])
    assert NUM_STEPS > 0
    assert NUM_BALLS > 0
except:
    usage()

# Drop ball in the galton box
def drop_ball():
    i, j = 0, 0
    for _ in range(NUM_STEPS):
        move = random.choice([move_left, move_right])
        i, j = move(i, j)
    return i, j


histogram = np.zeros(NUM_STEPS+1)
for _ in range(NUM_BALLS):
    i, j = drop_ball()
    assert i+j == NUM_STEPS
    # Note that we don't use j but we include it to make the simulation clearer
    histogram[i] += 1

#histogram[i] = num of balls fallen on sopt i
#box_distribution[i] = rate of balls fallen on spot i
box_distribution = histogram/NUM_BALLS
plt.bar(range(len(box_distribution)), box_distribution)


# Normal distribution
n = NUM_STEPS
mu = n/2
sigma = np.sqrt(n/4)
x = np.linspace(0, n, 100)
normal_pdf = norm.pdf(x, mu, sigma) #normal probability density function
plt.plot(x, normal_pdf, color='black')

# Labels and title
plt.xlabel('$i$')
plt.ylabel('$P[X=i]$')
plt.title(f'Galton box with {NUM_BALLS} balls and {NUM_STEPS} steps')

# Display the plot
plt.show()



# UNCOMMENT THIS TO SAVE THE FIGURE IN ../plots/ DIRECTORY:

# import os

# def new_filename(base, extension):
#     #name = base + '.' + extension
#     name = '.' #always exists
#     suffix_id = 0
#     while os.path.exists(name):
#         name = (base
#             + '-' + chr(ord('a')+suffix_id) 
#             + '.' + extension
#         )
#         suffix_id += 1
#     return name

# fn = new_filename(f'../plots/{sys.argv[1]}-{sys.argv[2]}', 'png')
# plt.savefig(fn)
# print(fn)