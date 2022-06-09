from collections import OrderedDict
from copy import deepcopy
from typing import Callable, Any
from pydantic import BaseModel


class Characteristics(BaseModel):
    b: Any
    b_dot: Any


class TimeMoments(BaseModel):
    time: float
    characteristics: Characteristics


class InterpolationByPoints:
    def __init__(self, data: list[TimeMoments]):
        self.data = data
        self.polynomial = OrderedDict()

    def get_interpolation_polynomial(self) -> Callable:
        for j in range(len(self.data) - 1):
            T_j = self.data[j].time
            dT_j = self.data[j + 1].time - T_j

            b_j = self.data[j].characteristics.b
            b_dot_j = self.data[j].characteristics.b_dot
            b_j1 = self.data[j + 1].characteristics.b
            b_dot_j1 = self.data[j + 1].characteristics.b_dot

            a0 = b_j
            a1 = b_dot_j
            a2 = (3 * b_j1 - 3 * b_j - 2 * b_dot_j * dT_j - b_dot_j1 * dT_j) / (dT_j**2)
            a3 = (2 * b_j + (b_dot_j + b_dot_j1) * dT_j - 2 * b_j1) / (dT_j**3)

            self.polynomial[T_j] = (
                deepcopy(a0),
                deepcopy(a1),
                deepcopy(a2),
                deepcopy(a3),
            )

        def _polynomial(t):
            for dt, coefficients in reversed(self.polynomial.items()):
                if t >= dt:
                    a0, a1, a2, a3 = coefficients
                    return a0 + a1 * (t - dt) + a2 * (t - dt) ** 2 + a3 * (t - dt) ** 3

        return _polynomial
