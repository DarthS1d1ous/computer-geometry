import math
from MathFunctions import *
from pointRelative import point_relative
from linesRelative import is_intersection
from Point import Point


def dimensionalTest(p, dot):
    xmin, ymin, xmax, ymax = min_and_max(p)
    if (dot.x < xmin or dot.x > xmax or dot.y < ymin or dot.y > ymax):
        return False
    return xmin


def ray_test(p, dot):
    S = 0
    # plt.scatter(q.x, q.y, marker='.', color='red')
    # plt.text(q.x + 0.05, q.y + 0.05, 'q', fontsize="15")
    # ray = Line(q, dot)
    # ray.drow_line()
    i = 0
    n = len(p)
    if dimensionalTest(p, dot):
        q = Point(dimensionalTest(p, dot) - 1, dot.y)
        while i < n:
            h = i
            if i == n - 1:
                h = 1
            p_tmp = p.copy()
            p_tmp.append(p[0])
            if is_intersection(q, dot, p_tmp[i], p_tmp[i + 1]):
                if point_relative(q, dot, p_tmp[i]) == 0:
                    if point_relative(q, dot, p_tmp[i + 1]) == 0:
                        if point_relative(q, dot, p_tmp[i - 1]) == point_relative(q, dot, p_tmp[h + 2]):
                            S += 1
                            # i = i + 1
                    else:
                        if point_relative(q, dot, p_tmp[i - 1]) == point_relative(q, dot, p_tmp[i + 1]):
                            S += 1
                else:
                    S += 1
                    # i = i + 1
            i += 1
        if S % 2 == 0:
            return False
        else:
            return True
    else:
        return False


def octane_test(p, dot):
    S = 0
    if dimensionalTest(p, dot):
        for i in range(len(p) - 1):
            T1 = chek_octane(p[i], dot)
            T2 = chek_octane(p[i + 1], dot)
            T = T2 - T1
            if T > 4:
                T -= 8
            if T < -4:
                T += 8
            if T == 4 or T == -4:
                d = determinant(p[i], p[i+1], dot)
                if d < 0:
                    T = -4
                if d > 0:
                    T = 4
                if d == 0:
                    return 0
            S += T
        T1 = chek_octane(p[len(p) - 1], dot)
        T2 = chek_octane(p[0], dot)
        T = T2 - T1
        if T > 4:
            T -= 8
        if T < -4:
            T += 8
        if T == 4 or T == -4:
            d = determinant(p[0], p[len(p) - 1], dot)
            if d < 0:
                T = -4
            if d > 0:
                T = 4
            if d == 0:
                return 0
        S += T
        if S == 8 or S == -8:
            return 1
        elif S == 0:
            return -1
    return -1
