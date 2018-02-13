import datetime
from collections import namedtuple

Location = namedtuple('Location', ['x', 'y'])


class Point:
    """A point class which stores location and time data"""

    def __init__(self, location):
        self.location = location
        self.creation_time = datetime.datetime

    def __repr__(self):
        return "%.3f, %.3f, %s" % (self.location.x, self.location.y, str(self.creation_time.today()))

    def __str__(self):
        return "%.3f, %.3f, %s" % (self.location.x, self.location.y, str(self.creation_time.today()))
