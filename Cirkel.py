__author__ = 'warreee'

class Cirkel():
    def __init__(self, xco = 0, yco = 0, r = 0):
        self.xco = xco
        self.yco = yco
        self.r = r
        self.twee()
        self.vier()

    #Deze methode berekent de 2 hoekpunten van de lijnstukken voor in algoritme 2

    def twee(self):
        self.linksxco = self.xco - self.r
         #Enkel de x-coördinaten veranderen.
        self.linksyco = self.yco
        self.rechtsxco = self.xco + self.r
         #Enkel de x-coördinaten veranderen.
        self.rechtsyco = self.yco

    #Deze methode berekent de 4 hoekpunten van de 2 lijnstukken voor in algoritme 3
    #De vier hoekpunten worden als volgt genoemd:

    def vier(self):

         # lb = linksboven
        self.lbxco = self.linksxco
        self.lbyco = self.yco + self.r

        # lo = linksonder
        self.loxco = self.linksxco
        self.loyco = self.yco - self.r

        # rb = rechtsboven
        self.rbxco = self.rechtsxco
        self.rbyco = self.yco + self.r

        # ro = rechtsonder
        self.roxco = self.rechtsxco
        self.royco = self.yco + self.r