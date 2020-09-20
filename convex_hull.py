# Program to gift wrap or perform Jarvis march for a random set of points
# Author: Vignesh Rajendiran

# Used pygame to visualize the final result
# The complexity is termed as O(nh) and sometimes O(n*n)

import random
import pygame

pygame.init()

WIDTH = 800
HEIGHT = 800

win = pygame.display.set_mode((WIDTH, HEIGHT))

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

win.fill(black)

pygame.display.set_caption("Convex hull using Jarvis March")

gameMode = False


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Checking if the three given points are clockwise, counterclockwise or co-linear with the help of slope
def orientation(p, q, r):
    if (q.y - p.y) * (r.x - q.x) - (r.y - q.y) * (q.x - p.x) < 0:
        return 1
    else:
        # either clockwise or co-linear
        return 0


# To identify the points of the convex hull
def convexHull(points, n):
    if n < 3:
        print("Please enter more than three points for a convex hull")
        return

    StartPoint = 0
    hull = []

    for i in range(1, n):
        if points[i].x < points[StartPoint].x:
            StartPoint = i

    p = StartPoint
    while True:

        hull.append(points[p])

        q = (p + 1) % n

        for i in range(0, n):
            if orientation(points[p], points[i], points[q]):
                q = i

        p = q

        if p == StartPoint:
            break

    # To display all the random points
    for j in range(0, n):
        pygame.draw.circle(win, white, (points[j].x, points[j].y), 2, 1)

    # To display the convex hull points and the lines connecting them
    for i in range(0, len(hull)):
        # print(hull[i].x, hull[i].y)
        pygame.draw.circle(win, red, (hull[i].x, hull[i].y), 2, 1)
        line_next = (i + 1) % int(len(hull))
        pygame.draw.line(win, white, (hull[i].x, hull[i].y), (hull[line_next].x, hull[line_next].y))


def main():
    points = []

    i = 0
    while i < 500:
        points.append(Point(random.randint(200, 699), random.randint(200, 599)))
        i = i + 1

    convexHull(points, len(points))
    while i < 1500:
        # To stop pygame from closing the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                i = 2000
        pygame.display.update()


main()
