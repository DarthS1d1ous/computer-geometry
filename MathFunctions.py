import math


def determinant(p1, p2, p):
    d = (p2.x - p1.x) * (p.y - p1.y) - (p2.y - p1.y) * (p.x - p1.x)
    return d


def min_and_max(p):
    xmin = p[0].x
    ymin = p[0].y
    xmax = p[0].x
    ymax = p[0].y
    for i in range(len(p)):
        if (xmin > p[i].x):
            xmin = p[i].x
        if (xmax < p[i].x):
            xmax = p[i].x
        if (ymin > p[i].y):
            ymin = p[i].y
        if (ymax < p[i].y):
            ymax = p[i].y
    return xmin, ymin, xmax, ymax


def chek_octane(p, dot):
    tmp = 0
    x = p.x - dot.x
    y = p.y - dot.y
    if 0 <= y < x:
        tmp = 1
    if 0 < x <= y:
        tmp = 2
    if 0 <= -x < y:
        tmp = 3
    if 0 < y <= -x:
        tmp = 4
    if 0 <= -y < -x:
        tmp = 5
    if 0 < -x <= -y:
        tmp = 6
    if 0 <= x < -y:
        tmp = 7
    if 0 < -y <= x:
        tmp = 8
    return tmp


def length(p1, p2):
    return math.sqrt((p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y))


def angle(p1, p0, p2):
    ca = (p1.x - p0.x) * (p2.x - p0.x) + (p1.y - p0.y) * (p2.y - p0.y)
    ca = ca / (length(p1, p0) * length(p2, p0))
    ca = math.acos(ca)
    return ca


def cos_num(p1, p2):
    return (p2.x - p1.x) / length(p1, p2)


def min_of_points_of_y(points):
    min = points[0]
    for i in range(len(points)):
        if min.y == points[i].y and min.x > points[i].x:
            min = points[i]
        if min.y < points[i].y:
            min = points[i]
    return min


def max_of_points_of_y(points):
    max = points[0]
    for i in range(len(points)):
        if max.y == points[i].y and max.x > points[i].x:
            max = points[i]
        if max.y > points[i].y:
            max = points[i]
    return max


def min_of_points_of_x(points):
    max = points[0]
    for i in range(len(points)):
        if max.x == points[i].x and max.y > points[i].y:
            max = points[i]
        if max.x > points[i].x:
            max = points[i]
    return max


def max_of_points_of_x(points):
    max = points[0]
    for i in range(len(points)):
        if max.x == points[i].x and max.y < points[i].y:
            max = points[i]
        if max.x < points[i].x:
            max = points[i]
    return max


def triangle_area(p1, p2, p3):
    area = math.fabs(0.5 * determinant(p1, p2, p3))
    return area


def perimeter(points):
    points.append(points[0])
    P = 0
    for i in range(len(points) - 1):
        P += length(points[i], points[i + 1])
    return P
