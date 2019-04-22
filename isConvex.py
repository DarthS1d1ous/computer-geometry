from pointRelative import point_relative


def is_convex(p):
    s = 0
    g = 0
    n = len(p)
    for i in range(n):
        k = i + 2
        if (i == n - 2):
            k = 0
        if (i == n - 1):
            k = 1
            if point_relative(p[i], p[0], p[k]) < 0:
                s += 1
            if point_relative(p[i], p[0], p[k]) > 0:
                g += 1
        if i!=n-1:
            if point_relative(p[i], p[i + 1], p[k]) < 0:
                s += 1
            if point_relative(p[i], p[i + 1], p[k]) > 0:
                g += 1
        if g != 0 and s != 0:
            return False
    return True
