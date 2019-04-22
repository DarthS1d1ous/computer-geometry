from MathFunctions import determinant as dt


def point_relative(p1, p2, p):
    d = dt(p1, p2, p)
    if d < 0:
        return 1 #левее
    elif d > 0:
        return -1 #правее
    else:
        return 0
