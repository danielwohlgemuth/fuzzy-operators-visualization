from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np


# Intersection

def average(x, y):
    return (x + y) / 2


def product(x, y):
    return x * y


def limited_difference(x, y):
    return max(0, x + y - 1)


def drastic_intersection(x, y):
    if y == 1:
        return x
    elif x == 1:
        return y
    else:
        return 0


# Union

def average_2(x, y):
    return (2 * min(x, y) + 4 * max(x, y)) / 6


def algebraic_sum(x, y):
    return x + y - x * y


def boundary_sum(x, y):
    return min(1, x + y)


def drastic_union(x, y):
    if y == 0:
        return x
    elif x == 0:
        return y
    else:
        return 1


# Inference

def gaines(x, y):
    return 1 if x <= y else 0


def godel(x, y):
    return 1 if x <= y else y


def goguen(x, y):
    return 1 if x <= y else y / x


def kleene(x, y):
    return max(1 - x, y)


def reichenbach(x, y):
    return 1 - x + x * y


def klir_yuan(x, y):
    return 1 - x + (x ** 2) * y


def zadeh(x, y):
    return max(1 - x, min(x, y))


def lukasiewicz(x, y):
    return min(1, 1 - x + y)


modes = (
    ('Intersection', (
        ('Minimum', min),
        ('Average', average),
        ('Product', product),
        ('Limited difference', limited_difference),
        ('Drastic intersection', drastic_intersection),
    )),
    ('Union', (
        ('Maximum', max),
        ('Average', average_2),
        ('Algebraic sum', algebraic_sum),
        ('Boundary sum', boundary_sum),
        ('Drastic union', drastic_union),
    )),
    ('Inference', (
        ('Gaines', gaines),
        ('Godel', godel),
        ('Goguen', goguen),
        ('Kleene', kleene),
        ('Reichenbach', reichenbach),
        ('Klir-Yuan', klir_yuan),
        ('Zadeh', zadeh),
        ('Lukasiewicz', lukasiewicz),
    )),
)

for mode in modes:
    functions = mode[1]

    for fun in functions:
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        fig.canvas.set_window_title('{}: {}'.format(mode[0], fun[0]))
        ax.set_title('{}: {}'.format(mode[0], fun[0]))

        if mode[0] != 'Inference':
            plt.gca().invert_xaxis()

        # Make data (from 0 to 1 in 20 steps)
        X = np.linspace(0, 1, 20)
        Y = np.linspace(0, 1, 20)
        X, Y = np.meshgrid(X, Y)
        zs = np.array([fun[1](x, y) for x, y in zip(np.ravel(X), np.ravel(Y))])
        Z = zs.reshape(X.shape)

        # Plot the surface.
        # Colormap from https://matplotlib.org/users/colormaps.html#grayscale-conversion
        surf = ax.plot_surface(X, Y, Z, cmap=cm.jet)

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        # To generate the images
        # fig.savefig('images/{}_{}.png'.format(mode[0].lower(), fun[0].lower().replace(' ', '_')))
        # print('{} - images/{}_{}.png'.format(fun[0], mode[0].lower(), fun[0].lower().replace(' ', '_')))

plt.show()
