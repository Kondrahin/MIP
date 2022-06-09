import numpy as np

from graphics import plot_graphics
from interpolation import TimeMoments, Characteristics, InterpolationByPoints

data = [
    TimeMoments(
        time=0.0,
        characteristics=Characteristics(b=np.array([0, 0]), b_dot=np.array([0, 0])),
    ),
    TimeMoments(
        time=1.0,
        characteristics=Characteristics(b=np.array([0, 1]), b_dot=np.array([1, 0])),
    ),
    TimeMoments(
        time=2.0,
        characteristics=Characteristics(b=np.array([1, 1]), b_dot=np.array([0, -1])),
    ),
    TimeMoments(
        time=3.0,
        characteristics=Characteristics(b=np.array([1, 0]), b_dot=np.array([0, 0])),
    ),
]

interpolation = InterpolationByPoints(data)
func = interpolation.get_interpolation_polynomial()

plot_graphics(data, func)
