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



def menu():
    i = interface.choose(["Hypotenuse", "Side", "Squared hypotenuse", "Squared side"])

    if i == 0:
        floats = interface.get_floats(["a side", "b side"])
        hypotenuse(floats[0], floats[1])

    elif i == 1:
        floats = interface.get_floats(["hypotenuse", "other side"])
        side(floats[0], floats[1])

    elif i == 2:
        floats = interface.get_floats(["a side", "b side"])
        squared_hypotenuse(floats[0], floats[1])

    elif i == 1:
        floats = interface.get_floats(["hypotenuse", "other side"])
        side(floats[0], floats[1])

    else:
        pass

