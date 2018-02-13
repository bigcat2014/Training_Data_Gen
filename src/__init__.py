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
    x0 = 0
    x1 = 0.001
    y_intercept = expression(x0)
    y1 = expression(x1)
    slope = (y1 - y_intercept) / (x1 - x0)
    return expression, slope, y_intercept


# r = tolerance
# m = perpendicular slope

# r * sin(atan(m)) = Δy0
# r * cos(atan(m)) = Δx0

# center_x0 + Δx0 = x1
# center_y0 + Δy0 = y1

# abs(tolerance) / sqrt(m**2 + 1) = center_Δx0

# x1 + center_Δx0 = center_x1
# m * (x2) + b = center_y1

# repeat
def get_points():
    # Starting point is y-intercept
    center_x, center_y = 0, b
    slope_delta_x = 0.001
    inv_slope = -1/m
    for x in range(num_points):
        # Find a random offset as a radius from the point on the line
        r = uniform(-1 * abs(tolerance), abs(tolerance))

        # Find the x and y delta for r, chosen along the line perpendicular to the slope
        point_delta_x = r * cos(atan(inv_slope))
        point_delta_y = r * sin(atan(inv_slope))

        # Find the new x and y values relative to the origin
        point_x = center_x + point_delta_x
        point_y = center_y + point_delta_y

        # Find the x delta of the center point of a circle with radius 'tolerance'
        center_delta_x = abs(tolerance) / sqrt(inv_slope**2 + 1)

        # Find the new x and y values of the circle, with radius 'tolerance', along the line and intersecting
        # the previous x value at the point where the perpendicular line intersects the circle
        center_x = point_x + center_delta_x
        center_y = line_function(center_x)

        # Find the slope of the line at the new point
        y0 = line_function(point_x)
        y1 = line_function(point_x + slope_delta_x)
        inv_slope = slope_delta_x / -(y1 - y0)

        yield point.Location(x=point_x, y=point_y)


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
