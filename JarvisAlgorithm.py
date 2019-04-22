from MathFunctions import *
from pointRelative import point_relative


def jarvis_algorithm(points):
    ch = []

    points = points.copy()
    s0 = min_of_points_of_y(points)
    min = min_of_points_of_y(points)
    points.remove(s0)
    max = max_of_points_of_y(points)
    ch.append(s0)
    min_polar_angle = points[0]
    while (s0 != max):
        for i in range(len(points)):
            if points[i].y < s0.y:
                if cos_num(s0, min_polar_angle) < cos_num(s0, points[i]):
                    min_polar_angle = points[i]
        ch.append(min_polar_angle)
        s0 = min_polar_angle
        points.remove(min_polar_angle)
        min_polar_angle = max
    points.append(min)
    min_polar_angle = min
    while (max != min):
        for i in range(len(points)):
            if points[i].y > max.y:
                if cos_num(max, min_polar_angle) > cos_num(max, points[i]):
                    min_polar_angle = points[i]
        ch.append(min_polar_angle)
        max = min_polar_angle
        if (max == min):
            break
        points.remove(min_polar_angle)
        min_polar_angle = min
    ch.pop()
    return ch
