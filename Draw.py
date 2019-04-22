import Generate
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
from isinConvex import *
from ConvexHull import *
from JarvisAlgorithm import jarvis_algorithm
from SetDiameter import set_diameter
from QHAlgorithm import *
from DynamicConvexHullAlgorithm import dynamic_convex_hull_algorithm
from FindingNearestPairOfPoints import findingNearestPairOfPoints

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Computational Geometry")
size = [800, 800]


def draw_arrow(screen, colour, start, end, coord=False, arrow=False):
    my_font = pygame.font.SysFont('Comic Sans MS', 20)
    dist = 40
    pygame.draw.line(screen, colour, start, end, 2)
    rotation = math.degrees(math.atan2(start[1] - end[1], end[0] - start[0])) + 90
    if arrow:
        pygame.draw.polygon(screen, colour,
                            ((end[0] + 12 * math.sin(math.radians(rotation)),
                              end[1] + 12 * math.cos(math.radians(rotation))),
                             (end[0] + 12 * math.sin(math.radians(rotation - 120)),
                              end[1] + 12 * math.cos(math.radians(rotation - 120))),
                             (end[0] + 12 * math.sin(math.radians(rotation + 120)),
                              end[1] + 12 * math.cos(math.radians(rotation + 120)))))
    text_start = my_font.render("(%d, %d)" % (start[0], start[1]), False, BLACK)
    text_end = my_font.render("(%d, %d)" % (end[0], end[1]), False, BLACK)
    if coord:
        screen.blit(text_start, (start[0], start[1] - dist))
        screen.blit(text_end, (end[0], end[1] - dist))


def draw_lines(p, color, screen):
    for i in range((len(p)) - 1):
        pygame.draw.line(screen, color, (p[i].x, p[i].y), (p[i + 1].x, p[i + 1].y), 5)
    pygame.draw.line(screen, color, (p[len(p) - 1].x, p[len(p) - 1].y), (p[0].x, p[0].y), 5)


def draw_lab1_1(p1, p2, p):
    pygame.init()
    window = pygame.display.set_mode(size)
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        window.fill(WHITE)
        draw_arrow(window, RED, (p1.x, p1.y), (p2.x, p2.y), False, True)
        pygame.draw.line(window, RED, (p1.x, p1.y), (p2.x, p2.y), 5)
        pygame.draw.circle(window, BLUE, (p.x, p.y), 4)
        pygame.display.flip()

    pygame.quit()


def draw_lab1_2(p1, p2, p3, p4):
    pygame.init()
    window = pygame.display.set_mode(size)
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        window.fill(WHITE)

        draw_arrow(window, RED, (p1.x, p1.y), (p2.x, p2.y), False, True)
        draw_arrow(window, RED, (p3.x, p3.y), (p4.x, p4.y), False, True)
        pygame.display.flip()

    pygame.quit()


def draw_lab1_3(p):
    pygame.init()
    window = pygame.display.set_mode(size)
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        window.fill(WHITE)

        for i in range(len(p)):
            draw_arrow(window, RED, (p[i - 1].x, p[i - 1].y), (p[i].x, p[i].y))
        pygame.display.flip()
        pygame.display.flip()

    pygame.quit()


def draw_lab1_4(p):
    window = pygame.display.set_mode(size)
    pygame.init()
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        window.fill(WHITE)

        for i in range(len(p)):
            draw_arrow(window, RED, p[i - 1], p[i], False, True)
        pygame.display.flip()
        pygame.display.update()

    pygame.quit()


def draw_lab2(p, p0, q):
    window = pygame.display.set_mode(size)
    pygame.init()
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        window.fill(WHITE)

        draw_lines(p, RED, window)
        pygame.draw.circle(window, GREEN, (p0.x, p0.y), 3)
        draw_arrow(window, BLACK, (p0.x, p0.y), (q.x, q.y))

        pygame.display.update()

    pygame.quit()


def draw_lab3(convex_polygon, simple_polygon, points):
    window = pygame.display.set_mode(size)
    pygame.init()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        window.fill(WHITE)

        draw_lines(convex_polygon, GREEN, window)
        draw_lines(simple_polygon, RED, window)
        for i in range(len(points)):
            pygame.draw.circle(window, BLACK, (points[i].x, points[i].y), 3)
            if octane_test(simple_polygon, points[i]) == 1:
                points[i].v = 0
            p1, p2 = getSector(convex_polygon, points[i])
            if not is_in_convex(convex_polygon, points[i]):
                # bvector = [points[i].x + points[i].vector[0], points[i].y + points[i].vector[1]]
                # bvector = [convex_polygon[p2].x - convex_polygon[p1].x, convex_polygon[p2].y - convex_polygon[p1].y]
                # factor = 2 * (points[i].vector[0] * bvector[0] + points[i].vector[1] * bvector[1]) / (
                #         bvector[0] * bvector[0] + bvector[1] * bvector[1])
                # newvector = [bvector[0] * factor - points[i].vector[0], bvector[1] * factor - points[i].vector[1]]
                # points[i].alpha += round(newvector[0])
                # points[i].alpha += round(newvector[1])

                points[i].alpha += math.pi / 4
                # f=random.randrange(-1,2)
                # if f==-1:
                #     points[i].alpha -= math.pi / 4
                # if f==1:
                #     points[i].alpha +=math.pi/4
                # if f==0:
                #     points[i].alpha -=math.pi/3
                # if f==2:
                #     points[i].alpha +=math.pi/3
            #     if f < 0:
            # print(points[i].vector)
            points[i].move1()
        pygame.display.update()
        clock.tick(60)


def draw_lab4(points):
    window = pygame.display.set_mode(size)
    pygame.init()
    clock = pygame.time.Clock()
    ch = convex_hull_step_by_step(points)
    i = -1
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        window.fill(WHITE)
        # draw_lines(ch, GREEN, window)
        # for x in points:
        #     pygame.draw.circle(window, BLACK, (x.x, x.y), 3)
        clock.tick(10)
        if i < len(ch) - 1:
            i = i + 1
        draw_lines(ch[i], RED, window)

        for p in points:
            pygame.draw.circle(window, BLACK, (p.x, p.y), 3)
        pygame.display.update()

    pygame.quit()


def draw_lab5(points):
    window = pygame.display.set_mode(size)
    pygame.init()
    clock = pygame.time.Clock()
    ch = jarvis_algorithm(points)
    run = True
    # for p in ch:
    #     print(p.x, p.y)
    for i in range(len(ch)):
        for j in range(len(ch)):
            if i != j: print(length(ch[i], ch[j]))
    print("/////////////////////////////////")
    d = set_diameter(ch) + 50
    chs_move = []
    print(d)
    for i in range(len(ch)):
        chs_move.append(Point(ch[i].x, ch[i].y, random.randint(-5, 5), random.randint(-5, 5)))
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        window.fill(WHITE)
        draw_lines(chs_move, GREEN, window)
        for p in chs_move:
            pygame.draw.circle(window, BLACK, (p.x, p.y), 3)
        for i in range(len(chs_move)):
            for j in range(len(chs_move)):
                if i != j and length(chs_move[i], chs_move[j]) > d:
                    print(length(chs_move[i], chs_move[j]))
                    chs_move[i].vector = [chs_move[i].vector[0] * (-1), chs_move[i].vector[1] * (-1)]
                    # chs_move[j].vector = [chs_move[j].vector[0] * (-1), chs_move[j].vector[1] * (-1)]
                    break
            pygame.draw.circle(window, BLACK, (chs_move[i].x, chs_move[i].y), 3)
            chs_move[i].move2(size)

        pygame.display.update()
        clock.tick(30)
    pygame.quit()


def draw_lab6(points):
    window = pygame.display.set_mode(size)
    pygame.init()
    clock = pygame.time.Clock()
    run = True
    chs_move = []
    P = perimeter(QH_algorithm(points))
    for i in range(len(points)):
        chs_move.append(Point(points[i].x, points[i].y, random.randint(1, 2), random.randint(1, 2)))
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        window.fill(WHITE)

        for i in range(len(chs_move)):
            chs_move[i].move2(size)
            pygame.draw.circle(window, BLACK, (chs_move[i].x, chs_move[i].y), 5)
        ch = QH_algorithm(chs_move)
        draw_lines(ch, GREEN, window)
        print(perimeter(ch))
        if perimeter(ch) > P:
            for x in ch:
                index = chs_move.index(x)
                chs_move[index].vector = [chs_move[index].vector[0] * (-1), chs_move[index].vector[1] * (-1)]
        pygame.display.update()
        clock.tick(30)
    pygame.quit()


def draw_lab7(points):
    window = pygame.display.set_mode(size)
    pygame.init()
    clock = pygame.time.Clock()
    run = True
    ch = dynamic_convex_hull_algorithm(points)
    i = -1
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        window.fill(WHITE)

        clock.tick(1)
        if i < len(ch) - 1:
            i = i + 1
        # draw_lines(ch[i], RED, window)

        for p in points:
            pygame.draw.circle(window, BLACK, (p.x, p.y), 3)
        for j in range(len(ch[i])):
            draw_arrow(window, RED, [ch[i][j - 1].x, ch[i][j - 1].y], [ch[i][j].x, ch[i][j].y], True)
        # draw_lines(ch, GREEN, window)
        pygame.display.update()
    pygame.quit()


def draw_lab10(points):
    window = pygame.display.set_mode(size)
    pygame.init()
    run = True
    result = []
    print(findingNearestPairOfPoints(points, result))
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        window.fill(WHITE)
        draw_lines(result, RED, window)

        for p in points:
            pygame.draw.circle(window, BLACK, (p.x, p.y), 3)
        pygame.display.update()
    pygame.quit()
