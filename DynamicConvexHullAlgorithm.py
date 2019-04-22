from MathFunctions import *
from pointRelative import point_relative


def dynamic_convex_hull_algorithm(points):
    points = points.copy()
    ch = []
    result = []

    for i in range(len(points)):
        if i == 0:
            ch.append(points[i])
            ch_copy = ch.copy()
            result.append(ch_copy)
            continue
        if i == 1:
            if points[0] != points[1]:
                ch.append(points[1])
                ch_copy = ch.copy()
                result.append(ch_copy)
                continue

        if i == 2:
            if points[2] == points[0] or points[2] == points[1]:
                continue

            if points[0] == points[1] and points[0] != points[2]:
                ch.append(points[i])
                ch_copy = ch.copy()
                result.append(ch_copy)
                continue

            if point_relative(points[0], points[1], points[2]) == 0:
                if (points[1].x - points[0].x) * (points[2].x - points[0].x) + (points[1].y - points[0].y) * (
                        points[2].y - points[0].y) < 0:
                    ch.clear()
                    ch.append(points[1])
                    ch.append(points[2])
                    ch_copy = ch.copy()
                    result.append(ch_copy)
                    continue

                elif (points[0].x - points[1].x) * (points[2].x - points[1].x) + (points[0].y - points[1].y) * (
                        points[2].y - points[1].y) < 0:
                    ch.clear()
                    ch.append(points[0])
                    ch.append(points[2])
                    ch_copy = ch.copy()
                    result.append(ch_copy)
                    continue

                else:
                    ch.clear()
                    ch.append(points[0])
                    ch.append(points[1])
                    ch_copy = ch.copy()
                    result.append(ch_copy)
                    continue
            if point_relative(points[0], points[1], points[2]) == 1:
                ch.append(points[2])
                ch_copy = ch.copy()
                result.append(ch_copy)
                continue
            else:
                ch.pop()
                ch.append(points[2])
                ch.append(points[1])
                ch_copy = ch.copy()
                result.append(ch_copy)
                continue
        visible = []
        for j in range(len(ch)):
            tmp = ch.copy()
            tmp.append(tmp[0])
            if point_relative(tmp[j], tmp[j + 1], points[i]) == -1:
                # if tmp[j] not in visible:
                visible.append(tmp[j])
                # if tmp[j+1] not in visible:
                visible.append(tmp[j + 1])
                index = j + 1
        if len(visible) == 0:
            ch_copy = ch.copy()
            result.append(ch_copy)
        else:
            k = 0
            ch.insert(index, points[i])
            while k < len(visible)-1:
                if visible.count(visible[k]) == 2:
                    ch.remove(visible[k])
                    visible.remove(visible[k])
                    visible.remove(visible[k])

                k += 1
            ch_copy = ch.copy()
            result.append(ch_copy)

    return result
