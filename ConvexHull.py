from MathFunctions import *
from pointRelative import point_relative


def convex_hull(points):
    ch = []

    points = points.copy()
    s0 = min_of_points_of_y(points)
    points.remove(s0)
    for i in range(len(points)):
        for j in range(len(points)):
            if i != j and cos_num(s0, points[i]) > cos_num(s0, points[j]):
                points[i], points[j] = points[j], points[i]
    ch.append(s0)
    ch.append(points[0])

    points.remove(points[0])
    for i in range(len(points)):
        while len(ch) != 2 and point_relative(ch[-2], ch[-1], points[i]) != 1:
            ch.pop()
        ch.append(points[i])

    return ch


def convex_hull_step_by_step(points):
    result = []
    ch = []

    points = points.copy()
    s0 = min_of_points_of_y(points)
    points.remove(s0)
    for i in range(len(points)):
        for j in range(len(points)):
            if i != j and cos_num(s0, points[i]) > cos_num(s0, points[j]):
                points[i], points[j] = points[j], points[i]
    ch.append(s0)
    ch.append(points[0])
    ch_copy = ch.copy()
    result.append(ch_copy)

    points.remove(points[0])
    for i in range(len(points)):
        while len(ch) != 2 and point_relative(ch[-2], ch[-1], points[i]) != 1:
            ch.pop()
            ch_copy = ch.copy()
            result.append(ch_copy)
        ch.append(points[i])
        ch_copy = ch.copy()
        result.append(ch_copy)
    return result
