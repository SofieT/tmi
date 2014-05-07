__author__ = 'Ward Schodts en Robin Goots'

from Punt import Punt
from math import sqrt
from Segment import Segment


class Cirkel():

    def __init__(self, xco=0, yco=0, r=0):
        self.xco = xco
        self.yco = yco
        self.r = r
        self.twee()
        self.segment()


    def getXco(self):
        return self.xco

    def getYco(self):
        return self.yco

    def getR(self):
        return self.r

    def twee(self):
        """
        Deze methode berekent de 2 hoekpunten van de lijnstukken voor in algoritme 2
        """
        self.linksxco = self.xco - self.r
        self.linksyco = self.yco
        self.linksPunt = Punt(self.linksxco, self.linksyco, 0, self)

        self.rechtsxco = self.xco + self.r
        self.rechtsyco = self.yco
        self.rechtsPunt = Punt(self.rechtsxco, self.rechtsyco, 1, self)

    def segment(self):
        """
        Deze methode berekent het segment voor algoritme 3
        """
        lo = Punt(self.linksxco, self.linksyco - self.r)
        hi = Punt(self.linksxco, self.linksyco + self.r)

    def check_overlap(self, other_cirkel):
        """
        Checkt of deze cirkel overlapt met de andere cirkel
        """

        e = self.getXco() - other_cirkel.getXco()
        f = self.getYco() - other_cirkel.getYco()
        p = sqrt(e**2 + f**2)

        if self.getR() + other_cirkel.getR() < p:
            # Bereken snijpunten
            return False
        elif self.r > p + other_cirkel.r or other_cirkel.r > p + self.r:
            return False
        else:
            return True

    def calculate_intersections(self, other_cirkel):
        #return self.real2_calculate_intersections(other_cirkel)
        d = sqrt( (self.xco - other_cirkel.xco)**2 + (self.yco - other_cirkel.yco)**2 )

        a = (self.r**2 - other_cirkel.r**2 + d**2) / (2 * d)
        h = sqrt(self.r**2 - a**2)
        px = self.getXco() + (a * (other_cirkel.getXco() - self.getXco())) / d
        py = self.getYco() + (a * (other_cirkel.getYco() - self.getYco())) / d

        x1 = px + ( h * (other_cirkel.getYco() - self.getYco()) ) / d
        y1 = py - ( h * (other_cirkel.getXco() - self.getXco()) )  / d

        x2 = px - ( h * (other_cirkel.getYco() - self.getYco()) ) / d
        y2 = py + ( h * (other_cirkel.getXco() - self.getXco()) ) / d

        if x1 == x2 and y1 == y2:
            return (x1, y1),
        return (x1, y1),(x2, y2)

    def real_calculate_intersections(self, other_circle):
        d = sqrt( (self.xco - other_circle.xco)**2 + (self.yco - other_circle.yco)**2 )
        intermediate = (d + self.r + other_circle.r) * (d + self.r - other_circle.r) * (d - self.r + other_circle.r) + (-d + self.r + other_circle.r)
        delta = 0.25 * sqrt((d + self.r + other_circle.r) * (d + self.r - other_circle.r)
                            * (d - self.r + other_circle.r) + (-d + self.r + other_circle.r))
        x1 = (self.xco + other_circle.xco) / 2  +  ((self.xco - other_circle.xco) * (self.r**2 + other_circle.r**2)) / 2*d**2 + 2 * ((self.yco - other_circle.yco)/d**2) * delta
        x2 = (self.xco + other_circle.xco) / 2  +  ((self.xco - other_circle.xco) * (self.r**2 + other_circle.r**2)) / 2*d**2 - 2 * ((self.yco - other_circle.yco)/d**2) * delta

        y1 = (self.yco + other_circle.yco) / 2  +  ((other_circle.yco - self.yco) * (self.r**2 + other_circle.r**2)) / 2*d**2 - 2 * ((self.xco - other_circle.xco)/d**2) * delta
        y2 = (self.yco + other_circle.yco) / 2  +  ((other_circle.yco - self.yco) * (self.r**2 + other_circle.r**2)) / 2*d**2 + 2 * ((self.xco + other_circle.xco)/d**2) * delta

        if x1 == x2 and y1 == y2:
            return (x1, y1),
        return (x1, y1),(x2, y2)

    def real2_calculate_intersections(self, other_cirkel):

        e = abs(self.xco - other_cirkel.xco)
        f = abs(self.yco - other_cirkel.yco)
        p = sqrt( e**2 + f**2 )

        k = abs(p**2 + self.r**2 - other_cirkel.r**2) / (2 * p)


        x1 = self.xco + (e*k)/p + (f/p)*sqrt(abs(self.r ** 2 - k ** 2))
        y1 = self.yco - (f*k)/p - (e/p)*sqrt(abs(self.r ** 2 - k ** 2))

        x2 = self.xco - (e*k)/p + (f/p)*sqrt(abs(self.r ** 2 - k ** 2))
        y2 = self.yco + (f*k)/p - (e/p)*sqrt(abs(self.r ** 2 - k ** 2))

        if x1 == x2 and y1 == y2:
            return (x1, y1),
        return (x1, y1),(x2, y2)

    def get_last_intersection(self):
        return self.last_x, self.last_y

