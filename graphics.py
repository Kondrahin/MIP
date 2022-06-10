from typing import Callable

import numpy as np
from matplotlib import pyplot as plt

from interpolation import TimeMoments

STEP = 0.01


def plot_graphics(data: list[TimeMoments], function: Callable):
    figure, axis = plt.subplot_mosaic(
        [["upleft", "right"], ["lowleft", "right"]], layout="constrained"
    )

    times_moments = [times_moment.time for times_moment in data]
    x = np.arange(min(times_moments), max(times_moments), step=STEP)
    y = np.array(list(map(function, x)))

    axis["upleft"].plot(x, y)
    axis["upleft"].legend(["x", "y"])
    axis["upleft"].set_title("Coordinates")

    y_dot = []
    for i in range(len(x) - 1):
        y_dot.append([(y[i + 1][0] - y[i][0]) / STEP, (y[i + 1][1] - y[i][1]) / STEP])

    axis["lowleft"].plot(x[:-1], y_dot)
    axis["lowleft"].legend(["x_dot", "y_dot"])
    axis["lowleft"].set_title("Speed")

    axis["right"].plot(y[:, 0], y[:, 1])
    axis["right"].set_title("Path")
    coordinates = [moment.characteristics.b for moment in data]
    coordinates_x = [coordinate[0] for coordinate in coordinates]
    coordinates_y = [coordinate[1] for coordinate in coordinates]
    axis["right"].scatter(coordinates_x, coordinates_y)
    for coordinate_x, coordinate_y in zip(coordinates_x, coordinates_y):
        text = f"({coordinate_x},{coordinate_y})"
        axis["right"].text(coordinate_x - 0.06, coordinate_y + 0.05, text, weight="bold")

    plt.gcf().canvas.set_window_title("Graphics")
    plt.show()
