from MathFunctions import *


def set_diameter(points):
    points = points.copy()
    k = len(points) - 1
    d = 0
    j = 1
    i = 1
    start = 0
    end = 0
    new_points = []
    points.append(points[0])
    while triangle_area(points[k], points[0], points[i]) < triangle_area(points[k], points[0], points[i + 1]):
        start = i
        j = 1
        i += 1
    while j < k+1:
        i = start
        while triangle_area(points[j], points[j + 1],
                            points[i]) <= triangle_area(points[j], points[j + 1], points[i + 1]):
            end = i
            i += 1
            if i > k:
                i = i-k
        new_points = points[start:end+1]
        for t in range(len(new_points)):
            if length(points[j], points[t]) > d:
                d = length(points[j], points[t])
            start = end
        j += 1
    return d

