import datetime
from collections import namedtuple

Location = namedtuple('Location', ['x', 'y'])


class Point:
    """A point class which stores location and time data"""

    def __init__(self, location):
        self.location = location
        self.creationTime = datetime.datetime
