import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def move_left(i, j):
    return (i+1, j)

def move_right(i, j):
    return (i, j+1)

NUM_STEPS = 6
NUM_BALLS = 8000

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


# Normal distribution approximation
n = NUM_STEPS
mu = n/2
sigma = np.sqrt(n/4)
x = np.linspace(0, n, 100)
normal_pdf = norm.pdf(x, mu, sigma) #normal probability density function
plt.plot(x, normal_pdf, color='black')

# Labels and title
plt.xlabel('$k$')
plt.ylabel('$P[X=k]$')
plt.title('')

# Display the plot
plt.show()