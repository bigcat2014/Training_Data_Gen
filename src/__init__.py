import matplotlib.pyplot as plt
import numpy as np
from math import *
import point
from random import uniform


def create_function(function_representation):
    def expression(x):
        try:
            # Evaluate the function
            # WARNING: Unsafe implementation
            return eval(function_representation)
        except:
            # return a line with slope of 1
            return x

    # Get slope and y-intercept at 0
    delta_x = 0.001

    y0 = expression(0)
    y1 = expression(delta_x)

    slope = (y1 - y0) / delta_x

    return expression, slope, y0


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
        y0 = line_function(center_x)
        y1 = line_function(center_x + slope_delta_x)
        delta_y = -(y1 - y0)
        inv_slope = (slope_delta_x / delta_y) if delta_y > 0.0001 else 0

        yield point.Location(x=point_x, y=point_y)


def main():
    # Step to get smooth lines
    step = pi/1024
    # Generator object for creating points
    next_point = get_points()

    # lists for x and y values of the points and the line function
    points_x = []
    points_y = []
    line_x = []
    line_y = []

    # Create all of the points and add their coordinates to the respective lists
    for x in range(num_points):
        p = point.Point(next(next_point, None))
        points_x.append(p.location.x)
        points_y.append(p.location.y)

    # Calculate the range of the data
    start = int(ceil(points_x[0]))
    length = int(ceil(points_x[num_points - 1]) / step)

    # Create list of y values to view the x-axis
    x_axis = np.zeros(abs(length) - start)

    # Create the lists of x and y values to display the function
    for x in range(start, abs(length)):
        line_x.append(x*step * (length / abs(length)))
        line_y.append(line_function(x*step) * (length / abs(length)))

    # Plot all lines and points
    plt.plot(line_x, line_y)
    plt.plot(line_x, x_axis)
    plt.plot(points_x, points_y)
    plt.scatter(points_x, points_y)
    plt.show()


if __name__ == "__main__":
    try:
        # Prompt user for line function
        line_function, m, b = create_function(input("Please enter a function:\n> "))
        # Prompt the user for the number of data points
        num_points = int(eval(input("Please enter the number of data points:\n> ")))
        # Prompt the user for the tolerance from the line the points should be generated
        tolerance = float(eval(input("Please enter the tolerance from the line:\n> ")))
    except:
        exit(1)
    main()
