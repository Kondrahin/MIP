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

    plt.gcf().canvas.set_window_title("Graphics")
    plt.show()
