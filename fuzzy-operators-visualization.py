import matplotlib
import matplotlib.pyplot as plt
import numpy as np

TILES = 20
# Colormap reference at https://matplotlib.org/stable/users/explain/colors/colormaps.html
COLOR_MAP = 'turbo'
SAVE_IMAGES = False
SHOW_IMAGES = True

modes = (
    ('Intersection', (
        ('Minimum', 'min(x, y)'),
        ('Average', '(x + y)/2'),
        ('Product', 'x * y'),
        ('Limited difference', 'max(0, x + y - 1)'),
        ('Drastic intersection', 'x if y == 1 else y if x == 1 else 0'),
    )),
    ('Union', (
        ('Maximum', 'max(x, y)'),
        ('Average', '(2*min(x, y) + 4*max(x, y))/6'),
        ('Algebraic sum', 'x + y - x*y'),
        ('Boundary sum', 'min(1, x + y)'),
        ('Drastic union', 'x if y == 0 else y if x == 0 else 1'),
    )),
    ('Inference', (
        ('Gaines', '1 if x <= y else 0'),
        ('Godel', '1 if x <= y else y'),
        ('Goguen', '1 if x <= y else y/x'),
        ('Kleene', 'max(1 - x, y)'),
        ('Reichenbach', '1 - x + x*y'),
        ('Klir-Yuan', '1 - x + (x**2) * y'),
        ('Zadeh', 'max(1 - x, min(x, y))'),
        ('Lukasiewicz', 'min(1, 1 - x + y)'),
    )),
)

for mode in modes:
    functions = mode[1]

    for fun in functions:
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        fig.canvas.manager.set_window_title('{}: {}'.format(mode[0], fun[0]))
        ax.set_title('{}: {} [{}]'.format(mode[0], fun[0], fun[1]))

        if mode[0] != 'Inference':
            plt.gca().invert_xaxis()

        # Make data (from 0 to 1 in TILES steps)
        X = np.linspace(0, 1, TILES)
        Y = np.linspace(0, 1, TILES)
        X, Y = np.meshgrid(X, Y)
        zs = np.array([eval(fun[1]) for x, y in zip(np.ravel(X), np.ravel(Y))])
        Z = zs.reshape(X.shape)

        # Plot the surface.
        surf = ax.plot_surface(X, Y, Z, cmap=COLOR_MAP)

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        # To generate the images
        if SAVE_IMAGES:
            fig.savefig('images/{}_{}.png'.format(mode[0].lower(), fun[0].lower().replace(' ', '_')))
            if not SHOW_IMAGES:
                matplotlib.pyplot.close()

if SHOW_IMAGES:
    plt.show()
