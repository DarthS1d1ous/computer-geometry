import random
from isSimple import is_simple
from Point import Point


def generate_random_point(min, max):
    return Point(random.randint(min, max), random.randint(min, max))


def generate_simple_polygon(min, max, n=6):
    p = []
    simple = False
    while not simple:
        p = [generate_random_point(min, max) for _ in range(n)]
        if is_simple(p):
            simple = True

    return p
