__author__ = 'warreee'

from Punt import Punt

class Cirkel():
    def __init__(self, xco = 0, yco = 0, r = 0):
        self.xco = xco
        self.yco = yco
        self.r = r
        self.twee()
        self.vier()

    def getXco(self):
        return self.xco

    def getYco(self):
        return self.yco

    #Deze methode berekent de 2 hoekpunten van de lijnstukken voor in algoritme 2
    def twee(self):
        linksxco = self.xco - self.r
        linksyco = self.yco
        self.linksPunt = Punt(linksxco, linksyco, 0)

        rechtsxco = self.xco + self.r
        rechtsyco = self.yco
        self.rechtsPunt = Punt(rechtsxco, rechtsyco, 1)

    #Deze methode berekent de 4 hoekpunten van de 2 lijnstukken voor in algoritme 3
    #De vier hoekpunten worden als volgt genoemd:

    def vier(self):

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

