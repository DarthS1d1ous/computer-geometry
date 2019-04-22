from pointRelative import point_relative
from linesRelative import is_intersection


def is_in_convex(p, dot):
    start = 0
    end = len(p) - 1
    if point_relative(p[0], p[1], dot) != point_relative(p[0], p[1], p[2]) or point_relative(
            p[len(p) - 1], p[0], dot) != point_relative(p[len(p) - 1], p[0], p[len(p) - 2]):
        return False
    while end - start > 1:
        sep = (start + end) // 2
        if point_relative(p[0], p[sep], dot) == point_relative(p[0], p[sep], p[1]):
            end = sep
        else:
            start = sep
    if is_intersection(p[start], p[end], p[0], dot):
        return False
    else:
        return True


def getSector(p, dot):
    start = 0
    end = len(p) - 1
    while end - start > 1:
        sep = (start + end) // 2
        if point_relative(p[0], p[sep], dot) == -1:
            start = sep
        else:
            end = sep
    return start, end
