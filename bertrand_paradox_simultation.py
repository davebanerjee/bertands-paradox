import numpy as np
from numpy import random
import matplotlib.pyplot as plt

def plot_chords(X, Y, approach_num):
    plt.figure(figsize=(6, 6))
    theta = np.linspace(0, 2*np.pi, 100)
    x_circle = np.cos(theta)
    y_circle = np.sin(theta)
    plt.plot(x_circle, y_circle, color='black', label='Unit Circle')
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    i = 0
    while i < len(X):
        x = [X[i], X[i+1]]
        y = [Y[i], Y[i+1]]
        plt.plot(x, y, marker=',', color='black', linewidth=0.25)
        i += 2
    if approach_num == 1:
        plt.title('Randomly Selected Chords Using Approach #1')
    elif approach_num == 2:
        plt.title('Randomly Selected Chords Using Approach #2')
    else:
        plt.title('Randomly Selected Chords Using Approach #3')

    plt.show()

def generate_random_points_on_circumference(num_points=2):
    if num_points % 2 != 0:
        print('Please input an even number of points.')
        return None
    X, Y = [], []
    for _ in range(num_points):
        theta = random.uniform(0, 2 * np.pi)  # Uniformly choose an angle between 0 and 2π
        x = np.cos(theta)
        y = np.sin(theta)
        X.append(x)
        Y.append(y)
    return X, Y

def generate_random_points_on_radius(num_chords=2):
    X, Y = [], []
    for _ in range(num_chords):
        midpoint = random.uniform(0,1)
        theta = random.uniform(0, 2*np.pi)
        # pre-rotation transformation
        x1 = np.sqrt(1 - midpoint ** 2)
        y1 = midpoint
        x2 = -1 * np.sqrt(1 - midpoint ** 2)
        y2 = midpoint

        # applying rotation transformation (see https://math.stackexchange.com/questions/2429/rotate-a-point-in-circle-about-an-angle)
        x1_rotated =      np.cos(theta) * x1 + np.sin(theta) * y1
        y1_rotated = -1 * np.sin(theta) * x1 + np.cos(theta) * y1
        x2_rotated =      np.cos(theta) * x2 + np.sin(theta) * y2
        y2_rotated = -1 * np.sin(theta) * x2 + np.cos(theta) * y2
        X.append(x1_rotated)
        X.append(x2_rotated)
        Y.append(y1_rotated)
        Y.append(y2_rotated)

    return X, Y

def generate_random_points_within_circle(num_chords=2):
    X, Y = [], []
    for _ in range(num_chords):
        # see how to generate points uniformly within a circle: https://stackoverflow.com/questions/5837572/generate-a-random-point-within-a-circle-uniformly
        r = np.sqrt(random.rand()) # we take sqrt here because circumference grows linearly with increasing radius, while area grows quadraticly with increasing radius
        theta = random.rand() * 2 * np.pi
        x_midpoint = r * np.cos(theta)
        y_midpoint = r * np.sin(theta)

        slope = -x_midpoint / y_midpoint

        # solving quadratic formula
        a = x_midpoint**2 + y_midpoint**2
        c = x_midpoint**2 + y_midpoint**2 - 1
        n = np.sqrt(-4*a*c) / (2*a)
        x1 = x_midpoint + n*y_midpoint
        y1 = y_midpoint - n*x_midpoint
        x2 = x_midpoint - n*y_midpoint
        y2 = y_midpoint + n*x_midpoint

        X.append(x1)
        X.append(x2)
        Y.append(y1)
        Y.append(y2)

    return X, Y


num_chords = 1500

# Approach 1 (random endpoints method)
num_endpoints = num_chords * 2
X, Y = generate_random_points_on_circumference(num_endpoints)
plot_chords(X, Y, approach_num=1)

# Approach 2 (random radius method)
X, Y = generate_random_points_on_radius(num_chords)
plot_chords(X, Y, approach_num=2)

# Approach 3 (random midpoint method)
X, Y = generate_random_points_within_circle(num_chords)
plot_chords(X, Y, approach_num=3)
