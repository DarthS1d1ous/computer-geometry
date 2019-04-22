from MathFunctions import *
from pointRelative import point_relative


def QH_algorithm(points):
    points = points.copy()
    sl = min_of_points_of_x(points)
    sr = max_of_points_of_x(points)
    SL = []
    SR = []
    square = 0
    max = 0
    min = 0
    SRnew = []
    SLnew = []
    ch = []
    ch.append(sl)
    # ch.append(sr)
    points.remove(sl)
    points.remove(sr)
    for i in range(len(points)):
        if point_relative(sl, sr, points[i]) != 1:
            SR.append(points[i])
        else:
            SL.append(points[i])

    # for i in range(len(SL)):
    #     if square < triangle_area(sl, sr, SL[i]):
    #         square = triangle_area(sl, sr, SL[i])
    #         max = SL[i]
    # ch.append(max)
    # SL.remove(max)
    # for i in range(len(SL)):
    #     if point_relative(sl, max, SL[i]) != -1:
    #         SLnew.append(SL[i])
    #     if point_relative(max, sr, SL[i]) != -1:
    #         SRnew.append(SL[i])

    recursion_for_qh_algorithm1(ch, SL, sl, sr)
    ch.append(sr)
    recursion_for_qh_algorithm2(ch, SR, sl, sr)
    # square = 0
    # sl = min_of_points_of_x(points)
    # sr = max_of_points_of_x(points)
    # for i in range(len(SR)):
    #     if square < triangle_area(sl, sr, SR[i]):
    #         square = triangle_area(sl, sr, SR[i])
    #         min = SR[i]
    # ch.append(min)
    # SR.remove(min)
    # recursion_for_qh_algorithm(ch, SRnew, SLnew, sr, min)
    return ch


def recursion_for_qh_algorithm1(ch, SL, sl, sr):
    if len(SL) == 0:
        return ch
    square = 0
    SRnew = []
    SLnew = []
    max = SL[0]
    for i in range(len(SL)):
        if square < triangle_area(sl, sr, SL[i]):
            square = triangle_area(sl, sr, SL[i])
            max = SL[i]
    # ch.append(max)
    SL.remove(max)
    for i in range(len(SL)):
        if point_relative(sl, max, SL[i]) != -1:
            SLnew.append(SL[i])
        if point_relative(max, sr, SL[i]) != -1:
            SRnew.append(SL[i])
    recursion_for_qh_algorithm1(ch, SLnew, sl, max)
    ch.append(max)
    recursion_for_qh_algorithm1(ch, SRnew, max, sr)

def recursion_for_qh_algorithm2(ch, SR, sl, sr):
    if len(SR) == 0:
        return ch
    square = 0
    SRnew = []
    SLnew = []
    max = SR[0]
    for i in range(len(SR)):
        if square < triangle_area(sl, sr, SR[i]):
            square = triangle_area(sl, sr, SR[i])
            max = SR[i]
    # ch.append(max)
    SR.remove(max)
    for i in range(len(SR)):
        if point_relative(sr, max, SR[i]) != -1:
            SLnew.append(SR[i])
        if point_relative(max, sl, SR[i]) != -1:
            SRnew.append(SR[i])

    recursion_for_qh_algorithm2(ch, SLnew, max, sr)
    ch.append(max)
    recursion_for_qh_algorithm2(ch, SRnew, sl, max)
    return ch


# def recursion_for_qh_algorithm1(ch, SL, SR, sl, sr):
#     if len(SL) == 0:
#         return ch
#     square = 0
#     SRnew = []
#     SLnew = []
#     max = SL[0]
#     for i in range(len(SL)):
#         if square < triangle_area(sl, sr, SL[i]):
#             square = triangle_area(sl, sr, SL[i])
#             max = SL[i]
#     # ch.append(max)
#     SL.remove(max)
#     for i in range(len(SL)):
#         if point_relative(sl, max, SL[i]) != -1:
#             SLnew.append(SL[i])
#         if point_relative(max, sr, SL[i]) != -1:
#             SRnew.append(SL[i])
#     recursion_for_qh_algorithm1(ch, SLnew, SRnew, sl, max)
#     ch.append(max)
#     recursion_for_qh_algorithm2(ch, SRnew, SLnew, max, sr)
#
#     ch.append(sr)
#
# def recursion_for_qh_algorithm2(ch, SL, SR, sl, sr):
#     if len(SR) == 0:
#         return ch
#     square = 0
#     SRnew = []
#     SLnew = []
#     max = SR[0]
#     for i in range(len(SR)):
#         if square < triangle_area(sl, sr, SR[i]):
#             square = triangle_area(sl, sr, SR[i])
#             max = SR[i]
#     # ch.append(max)
#     SR.remove(max)
#     for i in range(len(SR)):
#         if point_relative(sr, max, SR[i]) != -1:
#             SLnew.append(SR[i])
#         if point_relative(max, sl, SR[i]) != -1:
#             SRnew.append(SR[i])
#     recursion_for_qh_algorithm(ch, SLnew, SRnew, sl, max)
#     ch.append(max)
#     recursion_for_qh_algorithm(ch, SRnew, SLnew, max, sr)
#     return ch
