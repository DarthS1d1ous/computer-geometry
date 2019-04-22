from Generate import *
import pygame
import random
import math
from Point import Point
from Color import *
from pointRelative import point_relative
from linesRelative import is_intersection
from isSimple import is_simple
from isConvex import is_convex
from isinSimple import *
from Draw import *
from isinConvex import *
from QHAlgorithm import *
from  FindingNearestPairOfPoints import findingNearestPairOfPoints


def main_lab1_1():
    p1 = Point(random.randint(100, 700), random.randint(100, 700))
    p2 = Point(random.randint(100, 700), random.randint(100, 700))
    p = Point(random.randint(100, 700), random.randint(100, 700))
    point_relative_result = point_relative(p1, p2, p)
    if point_relative_result == 0:
        print("on line")
    else:
        if point_relative_result < 0:
            print("right")
        else:
            print("left")
    draw_lab1_1(p1, p2, p)


def main_lab1_2():
    p1 = Generate.generate_random_point(100, 700)
    p2 = Generate.generate_random_point(100, 700)
    p3 = Generate.generate_random_point(100, 700)
    p4 = Generate.generate_random_point(100, 700)
    if is_intersection(p1, p2, p3, p4):
        print("intersect")
    else:
        print("don't intersect")
    draw_lab1_2(p1, p2, p3, p4)


def main_lab1_3():
    x = random.randint(6, 10)
    p = [Generate.generate_random_point(100, 700) for _ in range(x)]
    if is_simple(p):
        print("simple")
    else:
        print("complex")
    draw_lab1_3(p)


def main_lab1_4():
    x = random.randint(6, 10)
    p = [Generate.generate_random_point(100, 700) for _ in range(x)]
    if is_convex(p):
        print("convex")
    else:
        print("concave")
    draw_lab1_4(p)


def main_lab2():
    # p = generate_simple_polygon(100, 700)
    # p0 = generate_random_point(100, 700)

    # p = [Point(200, 400), Point(400, 200), Point(600, 400), Point(400, 600)]
    # p0 = Point(300, 400)

    p = [Point(100, 200), Point(200, 200), Point(400, 100), Point(300, 400)]
    p0 = Point(400, 400)

    q = Point(dimensionalTest(p, p0) - 1, p0.y)

    print("angle test")
    if ray_test(p, p0):
        print("In polygon")
    else:
        print("Not in polygon")

    draw_lab2(p, p0, q)


def main_lab3():
    convex_polygon = [Point(200, 400), Point(250, 550), Point(400, 600), Point(550, 550), Point(600, 400),
                      Point(550, 250),
                      Point(400, 200), Point(250, 250)]
    simple_polygon = [Point(380, 450), Point(330, 425), Point(362, 415), Point(350, 410), Point(390, 390),
                      Point(375, 385),
                      Point(450, 350), Point(420, 392), Point(425, 395), Point(405, 420), Point(415, 425)]
    points = []
    i = 0
    while i < 20:
        x = random.randint(300, 500)
        y = random.randint(300, 500)
        points.append(Point(x, y))
        if is_in_convex(convex_polygon, points[i]) and octane_test(
                simple_polygon, points[i]) == -1:
            i += 1
            continue
        points.pop()
    draw_lab3(convex_polygon, simple_polygon, points)


def main_lab4():
    points = []
    i = 0
    while i < 50:
        x = random.randint(100, 700)
        y = random.randint(100, 700)
        points.append(Point(x, y))
        i += 1
    draw_lab4(points)


def main_lab5():
    points = []
    i = 0
    while i < 50:
        x = random.randint(200, 400)
        y = random.randint(200, 400)
        points.append(Point(x, y))
        i += 1
    draw_lab5(points)


def main_lab6():
    points = []
    i = 0
    while i < 50:
        x = random.randint(100, 600)
        y = random.randint(100, 600)
        points.append(Point(x, y))
        i += 1
    draw_lab6(points)


def main_lab7():
    points = []
    # points.append(Point(100, 200))
    # points.append(Point(50, 300))
    # points.append(Point(200, 400))
    # points.append(Point(150, 250))
    # points.append(Point(300, 220))
    # points.append(Point(20, 500))
    # points.append(Point(443,349))
    # points.append(Point(563, 101))
    # points.append(Point(511, 455))
    # points.append(Point(255, 203))
    # points.append(Point(365, 221))

    # points.append(Point(368, 400))
    # points.append(Point(303, 152))
    # points.append(Point(127, 288))
    # points.append(Point(361, 584))
    # points.append(Point(383, 510))
    # points.append(Point(330, 370))
    # points.append(Point(500, 430))
    i = 0
    while i < 17:
        x = random.randint(100, 600)
        y = random.randint(100, 600)
        points.append(Point(x, y))
        i += 1
    draw_lab7(points)

def main_lab10():
    points = []
    i = 0
    while i < 20:
        x = random.randint(100, 700)
        y = random.randint(100, 700)
        points.append(Point(x, y))
        i += 1
    draw_lab10(points)

if __name__ == "__main__":
    main_lab10()
