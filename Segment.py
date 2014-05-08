__author__ = 'Ward Schodts en Robin Goots'


class Segment():

    def __init__(self, lo, hi, circle):
        self.lo = lo
        self.hi = hi
        self.circle = circle

    def overlaps(self, segment):
        if self.lo < segment.lo:
            if self.hi > segment.lo:
                return True
