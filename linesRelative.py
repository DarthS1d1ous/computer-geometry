from MathFunctions import determinant as dt


def is_intersection(p1, p2, p3, p4):
    d1 = dt(p3, p4, p1)
    d2 = dt(p3, p4, p2)
    d3 = dt(p1, p2, p3)
    d4 = dt(p1, p2, p4)

    if (d1 == d2 == d3 == d4 == 0):
        if ((p3.x - p1.x) * (p4.x - p1.x) + (p3.y - p1.y) * (p4.y - p1.y) <= 0 or (p3.x - p2.x) * (p4.x - p2.x) + (
                p3.y - p2.y) * (p4.y - p2.y) <= 0 or (p1.x - p3.x) * (p2.x - p3.x) + (p1.y - p3.y) * (
                p2.y - p3.y) <= 0 or (p1.x - p4.x) * (p2.x - p4.x) + (p1.y - p4.y) * (p2.y - p4.y) <= 0):
            return True
        else:
            return False
    elif (d1 * d2 <= 0 and d3 * d4 <= 0):
        return True
    else:
        return False
