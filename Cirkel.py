__author__ = 'warreee'

class Cirkel:
    def __init__(self, xco = 0, yco = 0, r = 0):
        self.xco = xco
        self.yco = yco
        self.r = r
        self.twee()
        self.vier()

    #Deze methode berekent de 2 hoekpunten van de lijnstukken voor in algoritme 2
    #Enkel de x-coördinaten veranderen.
    def twee(self):
        self.linksxco = self.xco - self.r
        self.linksyco = self.yco
        self.rechtsxco = self.xco + self.r
        self.rechtsyco = self.yco

    #Deze methode berekent de 4 hoekpunten van de 2 lijnstukken voor in algoritme 3
    def vier(self):