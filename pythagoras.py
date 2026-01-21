import math

import interface


def squared_hypotenuse(a: float, b: float) -> float:
    return a**2 + b**2
def hypotenuse(a: float, b: float) -> float:
    return math.sqrt(squared_hypotenuse(a, b))


def squared_side(hypotenuse: float, other: float) -> float:
    return hypotenuse**2 - other**2

def side(hypotenuse: float, other: float) -> float:
    return math.sqrt(squared_side(hypotenuse, other))



