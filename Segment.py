__author__ = 'Ward Schodts en Robin Goots'



class Segment():

    def __init__(self, lo, hi, circle):
        self.lo = lo
        self.hi = hi
        self.circle = circle

    def overlaps(self, segment):
        if self.lo.yco < segment.lo.yco:
            if self.hi.yco >= segment.lo.yco:
                return True
            else:
                return False
        elif self.lo.yco == segment.lo.yco:
            return True
        else:
            if segment.hi.yco >= self.lo.yco:
                return True
            else:
                return False


