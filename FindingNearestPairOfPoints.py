import Point
from MathFunctions import *


def findingNearestPairOfPoints(points, result):
    points = points.copy()

    X = sorted(points, key=byX_key)
    Y = sorted(points, key=byY_key)

    return recursia(X, Y, result)


def recursia(X, Y, result):
    if len(X) < 4:
        if(len(X)>1):

            d = length(X[0], X[1])
        else: return 1000
        for i in range(len(X)):
            for j in range(len(X)):
                if i != j and length(X[i], X[j]) < d:
                    d = length(X[i], X[j])
                    if(len(result)!=0):
                        result.pop()
                        result.pop()
                    result.append(X[i])
                    result.append(X[j])
        return d
    sep = len(X) // 2
    Psep = X[sep]
    XL = X[0:sep]
    XR = X[sep + 1:len(X)]
    YL = []
    YR = []
    for i in range(len(Y)):
        if X[i].x > Psep.x:
            YR.append(X[i])
        if X[i].x < Psep.x:
            YL.append(X[i])
    dl = recursia(XL, YL, result)
    dr = recursia(XR, YR, result)
    d = min(dl, dr)
    Yliambda = []
    for i in range(len(Y)):
        if (Y[i].x - Psep.x) < d:
            Yliambda.append(Y[i])
    for i in range(len(Yliambda)):
        j = i
        k = 7
        if (len(Yliambda) - i) < 7:
            k = len(Yliambda) - i
        while j < i + k:
            if i != j and length(Yliambda[i], Yliambda[j]) <= d:
                d = length(Yliambda[i], Yliambda[j])
                if (len(result) != 0):
                    result.pop()
                    result.pop()
                result.append(Yliambda[i])
                result.append(Yliambda[j])
            j += 1

    return d


def byX_key(point):
    return point.x


def byY_key(point):
    return point.y
