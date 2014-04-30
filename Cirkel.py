__author__ = 'Ward Schodts en Robin Goots'

from Punt import Punt
from math import sqrt


class Cirkel():

    def __init__(self, xco = 0, yco = 0, r = 0, points = 0):
        self.xco = xco
        self.yco = yco
        self.r = r
        if points == 2:
            self.twee()
        elif points == 4:
            self.vier()


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
        linksxco = self.xco - self.r
        linksyco = self.yco
        self.linksPunt = Punt(linksxco, linksyco, 0, self)

        rechtsxco = self.xco + self.r
        rechtsyco = self.yco
        self.rechtsPunt = Punt(rechtsxco, rechtsyco, 1, self)

    def vier(self):
        """
        Deze methode berekent de 4 hoekpunten van de 2 lijnstukken voor in algoritme 3
        De vier hoekpunten worden als volgt genoemd:
        """
         # lb = linksboven
        lbxco = self.linksxco
        lbyco = self.yco + self.r
        self.lbPunt = Punt(lbxco, lbyco, 0, self.loPunt)

        # lo = linksonder
        loxco = self.linksxco
        loyco = self.yco - self.r
        self.loPunt = Punt(loxco, loyco, 0, self.lbPunt)

        # rb = rechtsboven
        rbxco = self.rechtsxco
        rbyco = self.yco + self.r
        self.rbPunt = Punt(rbxco, rbyco, 1, self.roPunt)

        # ro = rechtsonder
        roxco = self.rechtsxco
        royco = self.yco + self.r
        self.roPunt = Punt(roxco, royco, 1, self.rbPunt)

    def check_overlap(self, other_cirkel):
        """
        Checkt of deze cirkel overlapt met de andere cirkel
        """

        e = self.getXco() - other_cirkel.getXco()
        f = self.getYco() - other_cirkel.getYco()
        p = sqrt(e**2 + f**2)

        if self.getR() + other_cirkel.getR() <= p:
            # Bereken snijpunten
            return True
        else:
            return False

    def calculate_intersections(self, other_cirkel):
        d = (self.getR() + other_cirkel.getR())
        a = (self.getR()**2 - other_cirkel.getR() **2 + (d**2)) / (2 * d)
        h = sqrt( abs(self.getR()**2 - a**2))
        px = self.getXco() + (a * (other_cirkel.getXco() - self.getXco())) / d
        py = self.getYco() + (a * (other_cirkel.getYco() - self.getYco())) / d

        x1 = px + h * (other_cirkel.getYco() - self.getYco()) / d
        y1 = py - h * (other_cirkel.getXco() - self.getXco()) / d
        x2 = px - h * (other_cirkel.getYco() - self.getYco()) / d
        y2 = py + h * (other_cirkel.getXco() - self.getXco()) / d

        if x1 == x2 and y1 == y2:
            return (x1, y1),
        return (x1, y1),(x2, y2)


    def get_last_intersection(self):
        return self.last_x, self.last_y

