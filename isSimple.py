from linesRelative import is_intersection


def is_simple(p):
    n = len(p)
    k = 0
    for i in range(n - 1):
        m = n
        if (i == 0):
            m = n - 1
        for j in range(i + 2, m):
            if j == m - 1 and i!=0:
                if is_intersection(p[i], p[i + 1], p[j], p[0]):
                    k += 1
            else:
                if is_intersection(p[i], p[i + 1], p[j], p[j + 1]):
                    k += 1
    if k == 0:
        return True
    else:
        return False
