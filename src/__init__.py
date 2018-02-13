import matplotlib.pyplot as plt
import numpy as np
from math import *
import point
from random import uniform


def create_function(function_representation):
    def expression(x):
        try:
            return eval(function_representation)
        except:
            return x
    # Get slope and y-intercept at 0
    y_intercept = expression(0)
    y1 = expression(1)
    slope = y1 - y_intercept
    return expression, slope, y_intercept


def get_points():
    center_x, center_y = 0, 0
    inv_slope = -1/m
    for x in range(num_points):
        # Find a random offset as a radius from the point on the line
        r = uniform(-1 * abs(tolerance), abs(tolerance))

        point_delta_x = r * cos(atan(inv_slope))
        point_delta_y = r * sin(atan(inv_slope))

        point_x = center_x + point_delta_x
        point_y = center_y + point_delta_y

        center_delta_x = abs(tolerance) / sqrt(inv_slope**2 + 1)

        center_x = point_x + center_delta_x
        center_y = line_function(center_x)

        yield point.Location(x=point_x, y=point_y)

# r = tolerance
# m = perpendicular slope

# r * sin(atan(m)) = Δy0
# r * cos(atan(m)) = Δx0

# center_x0 + Δx0 = x1
# center_y0 + Δy0 = y1

# tolerance / (m + 1) = Δx1
# tolerance * m / (m + 1) = Δy1

# x1 + Δx1 = center_x1
# m * (x2) + b = center_y1

# repeat


def main():
    step = pi/1024
    next_point = get_points()

    points_x = []
    points_y = []
    line_x = []
    line_y = []

    for x in range(num_points):
        p = point.Point(next(next_point, None))
        points_x.append(p.location.x)
        points_y.append(p.location.y)

    length = int(ceil(points_x[len(points_x) - 1]) / step)
    x_axis = np.zeros(abs(length))
    for x in range(abs(length)):
        line_x.append(x*step * (length / abs(length)))
        line_y.append(line_function(x*step) * (length / abs(length)))

    plt.plot(line_x, line_y)
    plt.plot(line_x, x_axis)
    plt.plot(points_x, points_y)
    plt.scatter(points_x, points_y)
    plt.show()


if __name__ == "__main__":
    try:
        line_function, m, b = create_function(input("Please enter a function:\n> "))
        num_points = int(eval(input("Please enter the number of data points:\n> ")))
        # size = float(eval(input("Please enter the x range:\n> ")))
        tolerance = float(eval(input("Please enter the tolerance from the line:\n> ")))
    except:
        exit(1)
    main()
